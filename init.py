# from database.db import Base, Sessionlocal, engine
# from models.products import  Product
# import openpyxl

# def init_database():
#     Base.metadata.drop_all(bind=engine)  # удалить все таблички из БД
#     Base.metadata.create_all(bind=engine) # создать таблички в БД

#     # Заполняем таблицы

#     excel_file = 'export.xlsx'

#     p = []

#     try:
    
#         book = openpyxl.open(excel_file, read_only=True)
#         sheet = book.active

    
#         for row in range(2, 10): # sheet.max_row + 1
#             try:
            
#                 product_name = sheet[row][0].value
#                 article = sheet[row][1].value
#                 color = sheet[row][2].value
#                 length = sheet[row][7].value 
#                 width = sheet[row][8].value
#                 height = sheet[row][9].value
#                 quantity = sheet[row][31].value
#                 price = sheet[row][28].value
#                 link_1 = sheet[row][25].value
#                 link_2 = sheet[row][26].value
#                 link_3 = sheet[row][32].value
#                 link_4 = sheet[row][33].value

            
#                 data_row = [product_name, article, color, length, width, height, quantity, price, link_1, link_2, link_3, link_4]
#                 print(data_row)
#                 p.append(data_row)
#             except Exception as e:
#                 print(f"Error reading row {row}: {e}")
#                 continue

#     except FileNotFoundError:
#         print(f"Error: The Excel file '{excel_file}' was not found.")
#         exit()
#     except Exception as e:
#         print(f"An error occurred while reading the Excel file: {e}")
#         exit()
#     print(p)

#     session = Sessionlocal()

#     lst = Product(
#         product_name=product_name, 
#         article=article, 
#         color=color, 
#         length=length, 
#         width=width, 
#         height=height, 
#         quantity=quantity, 
#         price=price, 
#         link_1=link_1, 
#         link_2=link_2, 
#         link_3=link_3, 
#         link_4=link_4)

#     session.add_all(lst) # добовляем больше одной записи.
#     session.commit()
#     session.close()
