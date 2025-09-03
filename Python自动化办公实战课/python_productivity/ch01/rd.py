# import xlrd

# # file = '/Users/andyron/Downloads/a.xls'
# file = './ch01/a.xls'

# data = xlrd.open_workbook(file)
# table = data.sheets()[0]
# value = table.cell_value(rowx=4, colx=4)



import openpyxl

# file = '/Users/andyron/Downloads/a.xls'
file = './ch01/李雷.xlsx'

# 使用 openpyxl 读取 .xlsx 文件
wb = openpyxl.load_workbook(file)
sheet = wb.active
value = sheet.cell(row=5, column=5).value