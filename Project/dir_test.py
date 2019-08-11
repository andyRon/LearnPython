# -*- coding: utf-8 -*- 

# 检测指定目录是否存在，如果不存在就创建

# ref: https://github.com/geekcomputers/Python/blob/master/dir_test.py


from __future__ import print_function
import os

try:
	input = raw_input
except NameError:
	pass

def main():
	checkDir = input("Enter the name of the directory to check: ")

	if os.path.exists(checkDir):
		print("The directory exists")
	else:
		print("No directory found for " + checkDir)
		print()
		os.makedirs(checkDir)
		print("Directory created for " + checkDir)

if __name__ == '__main__':
	main()
