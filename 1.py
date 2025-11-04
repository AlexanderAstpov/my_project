import openpyxl
import sqlite3


book = openpyxl.open("export.xlsx", read_only=True)
sheet = book.active


print(sheet[1][1].value)
print()
p = []

for row in range(1,10): #sheet.max_row+1
    product_name = sheet[row][0].value
    article = sheet[row][1].value 
    color = sheet[row][2].value
    # print(row, product_name , article, color)
<<<<<<< HEAD
=======
    x = [row, product_name , article, color]
    p.append(x)
>>>>>>> af9d15970cf0aa480e23877a04abf0164f83e796




