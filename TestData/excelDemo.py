import openpyxl

book = openpyxl.load_workbook("/Users/sankalp/PycharmProjects/PythonSelFramework/PythonDemo.xlsx")
sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)
firstname = sheet.cell(row=2, column=2).value = "Sankalp"
print(firstname)

print(sheet.max_row)
print(sheet.max_column)

#another way to print values

print(sheet['A5'].value)
