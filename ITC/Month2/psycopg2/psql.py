import psycopg2
from dsn import connection

# cursor = connection.cursor()
# cursor.execute("CREATE TABLE laptop(id SERIAL PRIMARY KEY, name VARCHAR(50), price_som INTEGER, product_year INTEGER, exp_date_year INTEGER);")
# query = "INSERT INTO laptop(name, price_som, product_year, exp_date_year) VALUES ('hp', 15, 2020, 2022);"
# query = "ALTER TABLE laptop ADD COLUMN quantity INTEGER;"
# query = "UPDATE laptop SET name='Z', price_som=30, product_year=2022, exp_date_year=2027 WHERE id=2;"
# query = "UPDATE laptop SET name = 'Z' WHERE id=2;"
query = "SELECT name FROM laptop;"
cursor = connection.cursor()
cursor.execute(query)
date = cursor.fetchall()
print("Все наши товары: ")
# print(date)
lst=[]
for i in date:
    lst.append(*i)
print(*lst, sep=", ")

# name_of_product=input("Называния продукт : ")
# if name_of_product in lst:
#     query = f"SELECT quantity FROM laptop WHERE name='{name_of_product}';"
#     cursor.execute(query)
#     qty_db=cursor.fetchone()[0]
#     print(f"Количества продукта {name_of_product}: {qty_db}")
    
#     qty=int(input("Количество: "))
#     if qty_db >= qty:
#         upd_qty=qty_db - qty
#         query2 = f"UPDATE laptop SET quantity={upd_qty} WHERE name= '{name_of_product}'"
#         cursor.execute(query2)
#         connection.commit()
#         query3=f"SELECT price_som FROM laptop WHERE name='{name_of_product}';"
#         cursor.execute(query3)
#         connection.commit()
#         price_product = cursor.fetchone()[0] 
#         total_price= price_product*qty
#     n = input("Выберите товары которые хотите добавить: ")
#     n1 = int(input("Сколько вы хотите добавить: "))
#     if qty_db <= n1:
#         summ = qty_db + n1
#         query4 = f"UPDATE laptop SET quantity={summ} WHERE name='{n}';"
#         cursor.execute(query4)
#         connection.commit()
#         query5 = f"SELECT quantity FROM laptop WHERE name='{n}';"
#         cursor.execute(query4)
#         connection.commit()
#         date = cursor.fetchone()[0]
#         summm=date+n1
#         print(summm)
#     print(f"""
#                Количество:    {qty}
#                Ко-тво Итоговая: {summm} 
#                Цена:          {price_product}
#                Итоговая Цена: {total_price}
#             """)
# else:
#     print("Нет такого товара")    

# cursor.execute(query)
# connection.commit()
# cursor.close()
# connection.close()
name = int (input("""Для покупка введите 1: 
Чтобы добавить введите 2:
Чтобы добавить новый продукты введите 3: """))
if name == 1:
    n = input("Выберите продукта: ")
    query = f"SELECT quantity FROM laptop WHERE name='{n}';"
    cursor.execute(query)
    qty_db=cursor.fetchone()[0]
    print(f"Количества продукта {n}: {qty_db}")
    n1 = int(input("Сколько вы хотите купить: "))
    if qty_db >= n1:
        n3 = qty_db - n1
        query1 = f"UPDATE laptop SET quantity = {n3} WHERE name = '{n}';"
        cursor.execute(query1)
        connection.commit()
        date = cursor.fetchone()[0]
        d = date - n1
        print(d)
