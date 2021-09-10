#openpyxl_Test.py

import openpyxl

wb = openpyxl.Workbook()

#wb.save('test.xlsx')

sheet = wb.active
sheet1 = wb.active

sheet1.title = "1st"

sheet['A1'] = 'hello world!'
sheet.cell(row=3, column=3).value = 'bye!'

subject = ["python","java", "html", "javascript"]
sheet.append(subject)

wb.save('test.xlsx')