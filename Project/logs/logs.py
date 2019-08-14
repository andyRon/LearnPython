# -*- coding: utf-8 -*- 

"""
搜索指定目录下所有`*.log`文件，并压缩以日期格式保存
"""


import os
from time import strftime
import platform					# 获取操作系统各种信息
import sys


if platform.system() == 'Darwin' or platform.system() == 'Linux':
	pass
else:
	sys.exit()



logsdir = './'					# 日志目录
zip_program = 'zip'    			# 压缩程序
zipdir = './zip/'				# 压缩文件存储目录

for file in os.listdir(logsdir):
	if file.endswith('.log'):
		zipfile = file + '.' + strftime("%Y-%m-%d") + '.zip'   
		os.chdir(logsdir)															# 改变目录路径到指定位置
		os.system(zip_program + ' ' + os.path.join(zipdir, zipfile) + ' ' + file)	
		# os.remove(file)															# 删除原日志文件




