import xlsxwriter

wb = xlsxwriter.Workbook("../resources/xw.xlsx")
# 样式配置
titleFormat = wb.add_format({"bold": True})  # 加粗

headFormat = wb.add_format()
headFormat.set_bold()  # 加粗
headFormat.set_font_color("red")
headFormat.set_font_size(14)
headFormat.set_align("center")

dataFormat = wb.add_format()
dataFormat.set_bg_color("#808080")

sheet1 = wb.add_worksheet("我的工作表")
# 写入title以及表头
sheet1.write(0, 0, "2021年度", titleFormat)
sheet1.merge_range(1, 0, 2, 2, "第一季度销售统计", headFormat)
data = (["一月份", 500, 450], ["二月份", 600, 450], ["三月份", 700, 550])
sheet1.write_row(3, 0, ["月份", "预期销售额", "实际的销售额"], dataFormat)
# 写入数据
for index, item in enumerate(data):
    sheet1.write_row(index + 4, 0, item)
# 写入excel公式：计算 "预期销售额", "实际的销售额" 的和
sheet1.write(7, 1, "=sum(B5:B7)")
sheet1.write(7, 2, "=sum(C5:C7)")
sheet1.write_url(8, 0, "http://www.baidu.com", string="更多数据")
# 写入图表
chart = wb.add_chart({"type": "column"})  # 柱状图
chart.set_title({"name": "第一季度销售统计"})
# X,Y轴的描述信息
chart.set_x_axis({"name": "月份"})
chart.set_y_axis({"name": "销售额"})
# 数据
chart.add_series({
    "name": "预期销售额",
    "categories": "=我的工作表!$A$5:$A$7",
    "values": ["我的工作表", 4, 1, 6, 1]
})
chart.add_series({
    "name": "实际销售额",
    "categories": "=我的工作表!$A$5:$A$7",
    "values": ["我的工作表", 4, 2, 6, 2],
    "data_labels": {"value": True}
})
sheet1.insert_chart("A12", chart)

wb.close()
