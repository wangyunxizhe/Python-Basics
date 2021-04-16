import xlrd
from Mysqlhelper import *


# 试题类
class Question:
    pass


excel2 = xlrd.open_workbook("../resources/data2.xlsx")
sheet1 = excel2.sheet_by_index(0)
qList = []
for i in range(sheet1.nrows):
    if i > 1:
        obj = Question()
        obj.subject = sheet1.cell(i, 1).value  # excel中的“题目”列
        obj.questionType = sheet1.cell(i, 2).value  # excel中的“题型”列
        obj.optionA = sheet1.cell(i, 3).value  # 选项a
        obj.optionB = sheet1.cell(i, 4).value  # 选项b
        obj.optionC = sheet1.cell(i, 5).value  # 选项c
        obj.optionD = sheet1.cell(i, 6).value  # 选项d
        obj.score = sheet1.cell(i, 7).value  # 分值
        obj.answer = sheet1.cell(i, 8).value  # 正确答案
        qList.append(obj)

# 将excel中的数据导入到mysql中
db = dbhelper("127.0.0.1", 3306, "root", "870814", "python")
sql = "insert into question(subject,questionType,optionA,optionB,optionC,optionD,score,answer)" \
      "values(%s,%s,%s,%s,%s,%s,%s,%s)"
val = []
for item in qList:
    val.append((item.subject, item.questionType, item.optionA, item.optionB, item.optionC, item.optionD, item.score,
                item.answer))
db.executemanydata(sql, val)