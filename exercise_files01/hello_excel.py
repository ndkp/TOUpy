import openpyxl as excel

book = excel.Workbook()

sheet = book.active

sheet["A1"] = "こんにちは、Excel"

book.save("hello.xlsx")
