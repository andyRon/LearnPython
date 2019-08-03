# -*- coding: utf-8 -*- 

"""
统计给定文件夹的大小（遍历所有子文件夹和文件）


知识点：
`os.walk()`
结果为一个三元tupple， (dirpath, dirnames, filenames)
dirpath  string 目录的路径
dirnames list  子目录
filenames list  非目录

使用例子:
```python
python folder_size.py ../Project
Folder Size: 12215.0 Bytes
Folder Size: 11.93 Kilobytes
Folder Size: 0.01 Megabytes
Folder Size: 0.0 Gigabytes
```

"""

import os
import sys

try:
	directory = sys.argv[1]
except IndexError:
	sys.exit("Must provide")

dir_size = 0
fsizedicr = {'Bytes': 1, 
			 'Kilobytes': float(1) / 1024,
			 'Megabytes': float(1) / (1024 * 1024),
			 'Gigabytes': float(1) / (1024 * 1024 * 1024) 
			 }


for (path, dirs, files) in os.walk(directory):
	# print(files)
	# print(path)
	# print(dirs)
	# print('--------')
	for file in files:
		filename = os.path.join(path, file)
		dir_size += os.path.getsize(filename)

fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr]

if dir_size == 0: 
	print("Folder is Empty")
else:
	for units in sorted(fsizeList)[::-1]:
		print("Folder Size: " + units)