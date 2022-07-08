import openpyxl as excel

book = excel.Workbook()
sheet = book.active

for i in range(1,101):
    for j in range(1,101):
        cell = sheet.cell(i, j)
        cell.value = cell.coordinate

book.save("cellname100.xlsx")
