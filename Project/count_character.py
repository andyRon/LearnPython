# -*- coding: utf-8 -*- 

"""
统计文本文件中字符出现的次数

"""

import pprint  							# 数据美化输出
import collections

def main():
	file_input = input('File Name: ')
	try:
		with open(file_input, 'r') as info:
			counter = collections.Counter(info.read())	
	except FileNotFoundError:
		print("Please enter a valid file name.")
		main()

	# print(counter)
	print(pprint.pformat(count))
	exit()

if __name__ == '__main__':
	main()