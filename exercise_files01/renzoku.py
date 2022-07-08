import openpyxl as excel

book = excel.Workbook()
sheet = book.active

for i in range(10):
    sheet.cell(i+1,1,i)

book.save("renzoku.xlsx")
