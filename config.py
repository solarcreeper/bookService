#!/usr/bin/python
# -*- coding:utf-8 -*-
import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'some string'

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
