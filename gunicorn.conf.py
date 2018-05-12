# -*- coding: utf-8 -*-
# Author:William Zhang
# Email:quanpower@gmail.com
# Wechat:252527676
# Created:18-4-21 下午9:13

command = '/root/ENV/smartlink2/bin/gunicorn'
pythonpath = '/root/ENV/smartlink2/bin/'
bind = 'unix:/tmp/smartlink2.sock'
# bind = '0.0.0.0:8000'
workers = 5
user = 'root'