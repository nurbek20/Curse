import psycopg2
params = f"host={'localhost'} dbname = {'postgres'} user={'postgres'} password={'postgres'}"
connection=psycopg2.connect(params)
# cursor= connection.cursor()
# query = 'CREATE TABLE users(id SERIAL PRIMARY KEY, name TEXT, last_name TEXT);'
# cursor.execute(query)
# connection.commit()
# cursor.close()
# connection.close()
query = "SELECT productname FROM phons"
cursor= connection.cursor()
cursor.execute(query)
# date = cursor.fetchall()
# date = cursor.fetchone()
# date = cursor.fetchmany(3)
# print(date)
products = []
for i in cursor:
    products.append(*i)
    # print(*i)
print(products) 
   
productname = input("Что вы хотите купить? ")
if productname in products:
    print("Да имеется в наличии")
    n=f"SELECT productcount FROM phons WHERE productname={productname};"
    # cursor.execute(n)
    connection.commit()
    date=cursor.fetchall()
    print(f"Унас есть в наличии {date[0]} штук {n}")   
else:
    print("Не имеется в наличии")

connection.commit()
cursor.close()
connection.close()       