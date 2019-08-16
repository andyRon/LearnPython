# -*- coding: utf-8 -*- 

"""
统计文本文件中英文单词出现的次数

"""

import re


def main():
    file_input = input("File Name: ")
    wordstring = open(file_input).read()

    wordlist = re.compile(r'\b[a-zA-Z]+\b', re.I).findall(wordstring)

    wordfreq = [wordlist.count(w) for w in wordlist]                  # 生成统计数目的列表

    print("Pairs\n {}".format(str(dict(zip(wordlist, wordfreq)))))    # 生成字典

if __name__ == '__main__':
    main()




