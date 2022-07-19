# import psycopg2

# conn = psycopg2.connect(host= "localhost", 
#     port="5432", 
#     database="postgres", 
#     user="postgres", 
#     password="postgres")
# print("Успешно подключено к базе данных")

# cursor = conn.cursor()
# table_name = input("Введите называния таблица: ")
# query = f"CREATE TABLE {table_name}(id SERIAL PRIMARY KEY, name TEXT, author_id INTEGER REFERENCES author(id), wed_year INTEGER);"
# insert_query = "INSERT INTO author(name, birth_year) VALUES ('Антон Чехов', 1860), ('Владимир Набоков', 1899), ('Лев Толстой', 1828), ('Насон Грядущий', 3019), ('Александр Грибоедов', 1795), ('Александр Островсий', 1823), ('Марина Цветаева', 1892), ('Александр Герцен', 1812), ('Федор Достоевский', 1821), ('Николай Некрасов', 1821), ('Николай Чернышевский', 1828), ('Софья Ковалевская', 1850);"
# query = "SELECT * FROM author;"
# query = f"CREATE TABLE cafe(id SERIAL, title TEXT);" 
# udate = "UPDATE cafe SET title = 'Эки дос' WHERE id = 1;"
# cursor = connection.cursor()
# query = f"CREATE TABLE book(id SERIAL PRIMARY KEY, author_id INTEGER REFERENCES author(id), title TEXT, year INTEGER);"
# query = "INSERT INTO spouse(name, author_id, wed_year) VALUES ('Мария Бахметьева', 6, 1869), ('Фекла Викторова', 10, 1877), ('Сергей Эфрон', 7, 1912), ('Ольга Васильева', 11, 1853), ('Мария Исаева', 9, 1857), ('Наталья Захарьина', 8, 1838), ('Вера Слоним', 2, 1925), ('Софья Берс', 3, 1862), ('Нино Чарчавадзе', 5, 1828),('Ольга Книппер', 1, 1901), ('Владимир Ковалевский', 12, 1868), ('Анна Сниткина', 9, 1867);"
# query = "INSERT INTO book(author_id, title, year) VALUES (5, 'Горе от ума', 1824), (8, 'Кто виноват?', 1864), (7, 'Волшебнвй фонарь', 1912), (6, 'Утро молодого человека', 1850), (6, 'Бедная невеста', 1851), (8, 'Белые и думы', 1852), (11, 'Что делать?', 1863), (3, 'Зараженное семейство', 1864), (3, 'Нигилист', 1866), (10, 'Кому на Руси жить хорошо', 1877), (7, 'Вечерный альбом', 1910), (3, 'Власть тьмы, или Коготок увяз, всей птичке пропасть', 1886), (1, 'О вреде табака', 1886), (1, 'Иванов', 1887), (9, 'Крокадил', 1865), (9, 'Вечный муж', 1870), (1, 'трагик поневоле', 1889), (12, 'Воспоминания детства', 1890), (9, 'Записки из подполья', 1864), (2, 'Защита Лужина', 1930), (12, 'Воспоминания о Джордже Эллиоте', 1886), (2, 'Подвиг', 1932);"
# query = "INSERT INTO cafe(title) VALUES ('эки дос')"
# cursor.execute(query)
# date = cursor.fetchall()
# date = cursor.fetchone()
# date = cursor.fetchmany(3)
# print(date)
# conn.commit()
# cursor.close()
# conn.close()
# import needed, modules 
# import android 
# import time 
# import sys, select, os 
# for loop exit 
# Initiate android-module droid = android.Android() 
# notify me droid.makeToast("fetching GPS data") 
# print("start gps-sensor...") 
# droid.startLocating() 
# while True: 
#     exit loop hook if sys.stdin in select.select([sys.stdin], [], [], 0)[0]: 
#     line = input() print("exit endless loop...") 
#     break 
# wait for location-event event = droid.eventWaitFor('location',10000).result 
# if event['name'] == "location": 
#     try: 
#         try to get gps location data timestamp = repr(event['data']['gps']['time']) longitude = repr(event['data']['gps']['longitude']) latitude = repr(event['data']['gps']['latitude']) altitude = repr(event['data']['gps']['altitude']) speed = repr(event['data']['gps']['speed']) accuracy = repr(event['data']['gps']['accuracy']) loctype = "gps" 
#     except KeyError: 
#             if no gps data, get the network location instead (inaccurate) timestamp = repr(event['data']['network']['time']) longitude = repr(event['data']['network']['longitude']) latitude = repr(event['data']['network']['latitude']) altitude = repr(event['data']['network']['altitude']) speed = repr(event['data']['network']['speed']) accuracy = repr(event['data']['network']['accuracy']) loctype = "net" data = loctype + ";" + timestamp + ";" + longitude + ";" + latitude + ";" + altitude + ";" + speed + ";" + accuracy print(data) 
#             logging time.sleep(5) 
#             wait for 5 seconds 
#             print("stop gps-sensor...") droid.stopLocating()