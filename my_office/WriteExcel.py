import xlwt

# 第一步：创建工作簿
wb = xlwt.Workbook()
# 第二步：创建工作表1
ws = wb.add_sheet("CNY")
# 第三步：填充数据
# 表头（合并单元格）
titleStyle = xlwt.XFStyle()  # 初始化样式
titleFont = xlwt.Font()
titleFont.name = "宋体"
titleFont.bold = True  # 加粗
titleFont.height = 11 * 20
titleFont.colour_index = 0x08
titleStyle.font = titleFont
# 单元格对齐方式
cellAlign = xlwt.Alignment()
cellAlign.horz = 0x02  # 水平居中
cellAlign.vert = 0x01  # 垂直居中
titleStyle.alignment = cellAlign
# 边框
borders = xlwt.Borders()
borders.right = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DOTTED
titleStyle.borders = borders
# 背景颜色
dataStyle = xlwt.XFStyle()
bgcolor = xlwt.Pattern()
bgcolor.pattern = xlwt.Pattern.SOLID_PATTERN
bgcolor.pattern_fore_colour = 22  # 背景颜色
dataStyle.pattern = bgcolor
ws.write_merge(0, 1, 0, 5, "xlwt测试", titleStyle)
# 写入数据
data = (("日期", "A列", "B列", "C列", "D列", "E列"),
        ("15/04/2021", 8.1, 1, 0.8, 0.006, 6.222),
        ("16/04/2021", 8.2, 2, 0.7, 0.001, 6.111))
for i, tup in enumerate(data):
    for j, val in enumerate(tup):
        if j == 0:
            # i+2：跳过前两行（标题行），只有第一列才加入自定义样式
            ws.write(i + 2, j, val, dataStyle)
        else:
            ws.write(i + 2, j, val)
# 第四步：保存
wb.save("../resources/xlwt测试.xls")
