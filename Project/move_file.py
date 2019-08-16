# -*- coding: utf-8 -*- 

"""
把过期文件从源目录到目标目录(最近修改时间)


使用示例： ` python3 move_file.py -dst ./dst  -days 11`
```shell
$ python3 move_file.py -h
usage: python move_file.py -src [SRC] -dst [DST] -days [DAYS]

把过期文件从src目录移动到dst目录

optional arguments:
  -h, --help            show this help message and exit
  -src [SRC], --src [SRC]
                        将要被移动的文件目录，默认是当前目录
  -dst [DST], --dst [DST]
                        文件将要被移动的目录，必须填写
  -days [DAYS], --days [DAYS]
                        过期的最小天数，默认是240天
```

ref: https://github.com/geekcomputers/Python/blob/master/move_files_over_x_days.py
"""

import shutil
import sys
import time
import os
import argparse

usage = 'python move_file.py -src [SRC] -dst [DST] -days [DAYS]'
description = '把过期文件从src目录移动到dst目录'

args_parser = argparse.ArgumentParser(usage=usage, description=description)
args_parser.add_argument('-src', '--src', type=str, nargs='?', default='.', help='将要被移动的文件目录，默认是当前目录')
args_parser.add_argument('-dst', '--dst', type=str, nargs='?', required=True, help='文件将要被移动的目录，必须填写')
args_parser.add_argument('-days', '--days', type=int, nargs='?', default=240, help='过期的最小天数，默认是240天')
args = args_parser.parse_args()

if args.days < 0: 
	args.days = 0


if not os.path.exists(args.dst):
	os.mkdir(args.dst)

for f in os.listdir(args.src):
	if os.stat(f).st_mtime < time.time() - args.days * 86400:
		if os.path.isfile(f):
			shutil.move(f, args.dst)
