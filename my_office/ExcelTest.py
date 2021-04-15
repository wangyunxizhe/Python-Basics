import xlrd

data = xlrd.open_workbook("../resources/test.xlsx")
# ~~~~~~~~~~~~~~~~~~~~ xlrd的基本操作 ~~~~~~~~~~~~~~~~~~~~
# 获取所有的sheet
sheets = data.sheets()
print(sheets)
# 获取所有的sheet的名称
sheet_name = data.sheet_names()
print(sheet_name)
# 获取所有的sheet的数量
sheet_num = data.nsheets
print(sheet_num)
# 获取sheet1（方式1）
sheet1 = sheets[0]
print(sheet1)
# 获取sheet1（方式2）
sheet1 = data.sheet_by_index(0)
print(sheet1)
# 获取sheet1（方式3，根据名称）
# sheet1 = data.sheet_by_name("Sheet1")
print(sheet1)

# ~~~~~~~~~~~~~~~~~~~~ 操作excel的行 ~~~~~~~~~~~~~~~~~~~~
# 获取sheet1下有效行数的总数
rows = sheet1.nrows
print(rows)
print("该行单元格对象组成的列表：", sheet1.row(0))
print("获取指定行中每个单元格的数据类型：", sheet1.row_types(2))
print("获取指定单元格的value：", sheet1.row(0)[2].value)
print("获取指定行中所有单元格的value：", sheet1.row_values(1))
print("获取指定行的有效列数：", sheet1.row_len(1))

# ~~~~~~~~~~~~~~~~~~~~ 操作excel的列 ~~~~~~~~~~~~~~~~~~~~
print("sheet1下有效列的总数：", sheet1.ncols)
print("sheet1的第二列：", sheet1.col(1))
print("sheet1的第二列 第二行 单元格中的值：", sheet1.col(1)[1].value)
print("sheet1第二列单元格中所有值：", sheet1.col_values(2))
print("获取指定列中每个单元格的数据类型：", sheet1.col_types(2))

# ~~~~~~~~~~~~~~~~~~~~ 操作excel的单元格 ~~~~~~~~~~~~~~~~~~~~
print("获取二行三列 单元格中的值：", sheet1.cell(1, 2).value)
print("获取二行三列 单元格的数据类型：", sheet1.cell_type(1, 2))