import openpyxl as excel

book = excel.Workbook()
book.remove(book.worksheets[0])

for i in range(1, 21):
    sname = "シート" + str(i)
    sheet = book.create_sheet(title=sname)
    sheet["A1"].value = sname

book.save("sheet100.xlsx")
