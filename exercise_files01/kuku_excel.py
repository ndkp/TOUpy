import openpyxl as excel

book = excel.Workbook()
sheet = book.active

for i in range(1,10):
    for j in range(1,10):
        sheet.cell(i, j, i*j)

book.save("kuku.xlsx")
