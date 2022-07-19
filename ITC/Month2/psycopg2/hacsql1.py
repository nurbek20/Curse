import psycopg2

conn = psycopg2.connect(host= "localhost", 
    port="5432", 
    database="postgres", 
    user="postgres", 
    password="postgres")

cursor = conn.cursor()

query = 'SELECT name_of_product FROM products;'
cursor.execute(query)
product = []
for i in cursor:
    product.append(*i)
print(product)  
n=input("Выберите товарь: ")  
if n in product:
    n1 = f"SELECT  quantity_of_good, swholesale_price FROM products WHERE name_of_products='{n}'"
    cursor.execute(n1)
    conn.commit()
    data = cursor.fetchone()
    price_product = f"SELECT wholesale_price  FROM products WHERE name_of_product='{n}'"
    cursor.execute(price_product)
    conn.commit()
    data2 = cursor.fetchone()
    print(f"У нас в наличии есть {data[0]} штук {n}")
    phone_count =int(input("Сколько хотите купить?:"))
    count_price_product = int(data2[0]) * int(phone_count)