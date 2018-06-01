from flask import Flask
from config import config


def create_app(config_mode='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    config[config_mode].init_app(app)

    '''要在这里添加一些路由和自定义错误处理的信息，按照下文的说明，可以注册一个蓝本对象'''
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
