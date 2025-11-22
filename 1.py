import openpyxl
import sqlite3


excel_file = 'export.xlsx'
db_file = 'I_seller.db'


p = []

try:
  
    book = openpyxl.open(excel_file, read_only=True)
    sheet = book.active

   
    for row in range(2, 200): # sheet.max_row + 1
        quantity = sheet[row][31].value
        try:
            if quantity is not None and quantity == 0 or quantity == None:
                continue

            quantity = sheet[row][31].value
            product_name = sheet[row][0].value
            article = sheet[row][1].value
            color = sheet[row][2].value
            length = sheet[row][7].value 
            width = sheet[row][8].value
            height = sheet[row][9].value
            price = sheet[row][28].value
            link_1 = sheet[row][25].value
            link_2 = sheet[row][26].value
            link_3 = sheet[row][32].value
            link_4 = sheet[row][33].value

           
            data_row = [product_name, article, color, length, width, height, quantity, price, link_1, link_2, link_3, link_4]
            p.append(data_row)
        except Exception as e:
            print(f"Error reading row {row}: {e}")
            continue

except FileNotFoundError:
    print(f"Error: The Excel file '{excel_file}' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")
    exit()

print(p)

try:
   
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(500),
            article VARCHAR(50),
            color VARCHAR(50),
            len REAL, -- Changed to REAL to handle potential non-integer values
            width REAL,
            height REAL,
            quantity INTEGER,
            price INTEGER,
            link_1 TEXT,
            link_2 TEXT,
            link_3 TEXT,
            link_4 TEXT
        )
    ''')
    connection.commit()

    
    cursor.executemany('''
        INSERT INTO goods (name, article, color, len, width, height, quantity, price, link_1, link_2, link_3, link_4)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', p)
    connection.commit()

    print(f"Successfully inserted {len(p)} records into the '{db_file}' database.")

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
    if connection:
        connection.rollback() 
finally:
    
    if connection:
        connection.close()