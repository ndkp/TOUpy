import openpyxl as excel

book = excel.load_workbook(
    "uriage.xlsx", data_only=True)
sheet = book.active

data = []
for row in sheet["A3":"G28"]:
    values = [cell.value for cell in row]
    data.append(values)

data.sort(reverse=True, key=lambda x : x[5])

for row, row_val in enumerate(data):
    for col, val in enumerate(row_val):
        cell = sheet.cell(3+row, 1+col)
        cell.value = val

book.save("uriage_sort.xlsx")
