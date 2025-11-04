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
    x = [product_name , article, color]
    p.append(x)

print(p)

connection = sqlite3.connect('I_seller.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS goods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(500),
    article VARCHAR(50),
    color VARCHAR(50)
    )
    ''')

connection.commit()

cursor.executemany('''
INSERT INTO goods ('name', 'article', 'color') 
VALUES (?, ?, ?)          
''', p)

connection.commit()