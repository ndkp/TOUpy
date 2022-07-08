import openpyxl as excel

book = excel.load_workbook("cellname100.xlsx")
sheet = book.active

for i in range(2, 5):
    data = []
    for j in range(3, 7):
        cell = sheet.cell(i, j)
        data.append(cell.value)
    print(data)
