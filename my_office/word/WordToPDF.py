from win32com.client import constants, gencache
import os


def createPDF(wordPath, pdfPath):
    word = gencache.EnsureDispatch("Word.Application")
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    # 转换方法
    doc.ExportAsFixedFormaopenpyxlt(pdfPath, constants.wdExportFormatPDF)
    word.Quit()


print(os.listdir("../../resources"))
createPDF("../../resources/简介.docx", "../../resources/简介1.pdf")
