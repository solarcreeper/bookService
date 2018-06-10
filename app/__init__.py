#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask
from conf.config import config
from flask_login import LoginManager
import logging
from logging.config import fileConfig
import os

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
fileConfig('conf/log-app.conf')


def get_logger(name):
    return logging.getLogger(name)


def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))


def get_config():
    return config[os.getenv('FLASK_CONFIG') or 'default']


def create_app(config_mode='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    config[config_mode].init_app(app)

    login_manager.init_app(app)
    # 要在这里添加一些路由和自定义错误处理的信息，按照下文的说明，可以注册一个蓝本对象
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
