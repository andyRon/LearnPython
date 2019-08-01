# -*- coding: utf-8 -*-

"""
读取当前系统信息
"""

import platform as pl

# 数组中都是platform的方法名，可通过 dir(platform) 获取所有的查看
profile = [
    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version'
]

# 字体颜色、粗细等
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for key in profile:
    if hasattr(pl, key):
        print(key + bcolors.BOLD + ": " + str(getattr(pl, key)()) + bcolors.ENDC)
