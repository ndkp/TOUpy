import openpyxl as excel

book = excel.Workbook()
sheet = book.active

cell = sheet["AA5"]
print(f"AA5=({cell.row},{cell.column})")