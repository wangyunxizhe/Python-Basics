import xlrd
import xlsxwriter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 1，读取excel
data = xlrd.open_workbook("../resources/info.xlsx")
info = []
for sheet in data.sheets():
    dict = {"name": sheet.name, "avgsalary": 0}  # 班级信息
    sum = 0
    for i in range(sheet.nrows):
        # 第一行除外
        if i > 1:
            sum += float(sheet.cell(i, 5).value)  # 得到薪资数据
    # 计算平均薪资
    dict["avgsalary"] = sum / (sheet.nrows - 2)
    info.append(dict)
print(info)
# 2，将计算好的平均薪资写入到新的excel
wb = xlsxwriter.Workbook("../resources/newinfo.xlsx")
sheet = wb.add_worksheet()
# 写入班级数据
nameInfo = []
salaryInfo = []
for item in info:
    nameInfo.append(item["name"])
    salaryInfo.append(item["avgsalary"])
sheet.write_column("A1", nameInfo)
sheet.write_column("B1", salaryInfo)
# 写入图表
chart = wb.add_chart({"type": "column"})  # 柱状图
chart.set_title({"name": "平均就业薪资"})
chart.add_series({
    "name": "班级",
    "categories": "=Sheet1!$A$1:$A$3",
    "values": "=Sheet1!$B$1:$B$3"
})
sheet.insert_chart("A7", chart)
# 3，发送到指定邮箱
host_server = "smtp.qq.com"
sender = "543456229@qq.com"
code = "dajbsbinojdybecg"
user1 = "wangyuan0814@yeah.net"
# 准备邮件数据
# 邮件标题
mail_title = "！！！来自python端的邮件！！！"
# 邮件内容
mail_content = "附件测试：具体查看附件"
# 构建附件
attachment = MIMEApplication(open("../resources/newinfo.xlsx", "rb").read())
attachment.add_header("Content-Disposition", "attachment", filename="图表.xlsx")
smtp = smtplib.SMTP(host_server)
smtp.login(sender, code)
msg = MIMEMultipart()  # 带附件的消息实例
msg["Subject"] = mail_title
msg["From"] = sender
msg["To"] = user1
msg.attach(MIMEText(mail_content))
msg.attach(attachment)
smtp.sendmail(sender, user1, msg.as_string())

wb.close()
