#!/opt/homebrew/bin/python3

from PyQt6.QtCore import QDateTime, Qt

# 本地时间的当前时间
now = QDateTime.currentDateTime()

print('Local datatime: ', now.toString(Qt.DateFormat.ISODate))
print('Universal datatime: ', now.toUTC().toString(Qt.DateFormat.ISODate))

print(f'The offset from UTC is(本地时间与标准时间的差): {now.offsetFromUtc()} seconds')

print('Local datetime: ', now.toString(Qt.DateFormat.ISODate))