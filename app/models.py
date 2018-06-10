#!/usr/bin/python
# -*- coding:utf-8 -*-
from peewee import CharField, BooleanField, IntegerField
from werkzeug.security import check_password_hash
from app import login_manager, get_config


# 管理员工号
class User:
    def __init__(self, username):
        self.username = username
        self.email = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


# 通知人配置
class CfgNotify():
    check_order = IntegerField()  # 排序
    notify_type = CharField()  # 通知类型：MAIL/SMS
    notify_name = CharField()  # 通知人姓名
    notify_number = CharField()  # 通知号码
    status = BooleanField(default=True)  # 生效失效标识


class ConfigJob():
    job_id = IntegerField()
    job_name = CharField()
    job_content = CharField()


@login_manager.user_loader
def load_user(user_name):
    user = get_config().USERS_COLLECTION.find_one({"username": user_name})
    if user is not None:
        return User(user['username'])
    else:
        return None


if __name__ == '__main__':
    pass
