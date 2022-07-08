import openpyxl as excel

book = excel.load_workbook(
    "uriage.xlsx",
    data_only=True)
sheet = book.active

for row in sheet["A3":"G28"]:
    print([cell.value for cell in row])
