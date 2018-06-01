# -*- coding:utf8 -*-
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/web_root/bookService/")
from app import create_app
application= create_app()