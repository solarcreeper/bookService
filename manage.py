#!/usr/bin/python
# -*- coding:utf-8 -*-
from app import create_app

if __name__ == '__main__':
    my_app = create_app()
    my_app.debug = True
    my_app.run()
