#!/usr/bin/python
# -*- coding:utf-8 -*-
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return "hello world"
