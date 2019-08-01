# -*- coding: utf-8 -*- 

"""
在用户目录中检测某个目录是否存在，如果不存在，就创建
"""

import os

MESSAGE = "The directory already exists."
CREATEDIR = "testdir"


try:
	home = os.path.expanduser('~')

	dest_dir = os.path.join(home, CREATEDIR)

	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)
	else:
		print(MESSAGE)
except Exception as e:
	print(e)





