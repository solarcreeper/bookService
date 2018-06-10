#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

from pymongo import MongoClient


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret'
    DB_NAME = 'book_service'
    DATABASE = MongoClient()[DB_NAME]
    USERS_COLLECTION = DATABASE.user
    JOB_COLLECTION = DATABASE.job

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True


class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True


class ProductionConfig(Config):
    """生产环境配置"""
    TESTING = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
