# -*- coding:utf8 -*-
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/web_root/bookService/")
from manage import my_app as application