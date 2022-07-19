from itertools import count
import time
import psycopg2

connect = psycopg2.connect(host="localhost", 
port="5432", 
dbname="postgres",
user="postgres", 
password="postgres")

cursor = connect.cursor()

query = 'select productname from phons;'
cursor.execute(query)
product = []
for i in cursor:
    product.append(*i)
print(product)


print("Добро пожаловать дорогой покупатель в интернет магазин IB_shop!!!")
vybor = input("Что вы хотите купить?:")
if vybor in product:
    sec = f"SELECT productcount FROM phons WHERE productname='{vybor}'"
    cursor.execute(sec)
    connect.commit()
    data = cursor.fetchone()
    price_product = f"SELECT price FROM phons WHERE productname='{vybor}'"
    cursor.execute(price_product)
    connect.commit()
    data2 = cursor.fetchone()
    print(f"У нас в наличии есть {data[0]} штук {vybor}")
    phone_count =int(input("Сколько хотите купить?:"))
    count_price_product = int(data2[0]) * int(phone_count)
    if phone_count <= data[0]:
        seconds = time.time()
        dt = time.ctime(seconds)
        count_total = int(data[0])-int(phone_count)
        name = input("Ваше имя:")
        s_name = input("Ваша фамилия:")

        print(f"""                         IB_SHOP       
                       Кассовый чек
        ----------------------------------------
        {vybor}        {phone_count}x{data2[0]} ={count_price_product}
        ИТОГ                     ={count_price_product}
        ----------------------------------------

        Ф.И.О покупателя:    {name}{s_name}
        Оплачено:                {count_price_product}   
        Плат.картой              {count_price_product}
        Кассир                      Сист.Админ
        
        Дата покупки: {dt}
                         IB_SHOP                  
                    Спасибо за покупку!           """)
        query1 = f"INSERT INTO klients(purchases, when_bought, total, count_products, full_name) VALUES('{vybor}', '{dt}', '{count_price_product}', '{phone_count}', '{name} {s_name}')"
        query2 = f"UPDATE phons SET productcount = {count_total} WHERE productname='{vybor}';"
        cursor.execute(query1)
        connect.commit()
        cursor.execute(query2)
        connect.commit()
        cursor.close()
        connect.close()
    else:
        print(f"У нас нету {vybor} в таких колличевствах")
else:
    print("Телефон в данное время нету в наличии")