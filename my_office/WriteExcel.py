import xlwt

# 第一步：创建工作簿
wb = xlwt.Workbook()
# 第二步：创建工作表1
ws = wb.add_sheet("CNY")
# 第三步：填充数据
# 表头（合并单元格）
ws.write_merge(0, 1, 0, 5, "xlwt测试")
# 写入数据
data = (("日期", "A列", "B列", "C列", "D列", "E列"),
        ("15/04/2021", 8.1, 1, 0.8, 0.006, 6.222),
        ("16/04/2021", 8.2, 2, 0.7, 0.001, 6.111))
for i, tup in enumerate(data):
    for j, val in enumerate(tup):
        # i+2：跳过前两行（标题行）
        ws.write(i + 2, j, val)
# 第四步：保存
wb.save("../resources/xlwt测试.xls")
