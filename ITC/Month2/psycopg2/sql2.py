# import psycopg2
# n=int(input("""Для создания таблицы введите 1:
# Для записи введите 2:
# Если хотите изменит записи введите 3:
# Если хотите удалить таблица введите 4: 
# Для выхода введите 5: """))
# if n==1:
#     n1=input("Пишите называния таблица: ")
#     query=f"CREATE TABLE {n1}(id SERIAL PRIMARY KEY, name TEXT, age INTEGER, last_name TEXT );"
#     try:
#         cursor.execute(query)
#         print("Таблица успешно создан")
#     except psycopg2.errors.DuplicateTable:
#         print("Уже существует такая таблица")    
# # connection.commit()
# cursor.close()
# connection.close()  
import psycopg2

connection = psycopg2.connect(host="localhost", port="5432", dbname="postgres",user="postgres", password="postgres")

cursor = connection.cursor()

n = int(input("""Если хотите добавить запись введите 1:
Если хотите изменить столбца введите 2: 
Если хотите удалить запись введите 3:
Если хотите очистить таблицу введите 4:
Для Создания новую таблицу введите 5: 
Чтобы Открыть таблицу введите 6:
Для выхода введите 7:  """))
if n == 1:
    table1_name = input("Выберите таблицу: ")
    COLUMNS = input("Введите колоны через запятые: ").split(",")
    VALUES1 = input("Введите записи через запятые: ").split(",")
    query1 = f"INSERT INTO {table1_name}({COLUMNS[0]}, {COLUMNS[1]}, {COLUMNS[2]}) VALUES('{VALUES1[0]}', '{VALUES1[1]}', '{VALUES1[2]}')"
    try:
        cursor.execute(query1)
        print("Запись успешно добавлена!!!")
    except psycopg2.errors.UndefinedTable:
        print("Такой таблицы не существует!")
    except psycopg2.errors.UndefinedColumn:
        print("Таких колон не существует!")
    connection.commit()
elif n == 2:
    table2_name = input("Выберите таблицу: ")
    f_inp = input("Введите название столбца: ")
    s_inp = input("Как хотите изменить: ")
    t_inp = int(input("ID которую нужно изменить: "))
    query2 = f"UPDATE {table2_name} SET {f_inp} = '{s_inp}' WHERE id={t_inp};"
    try:
        cursor.execute(query2)
        print("Запись успешно изменена!")
    except psycopg2.errors.UndefinedTable:
        print("Такой таблицы не существует!")
    except psycopg2.errors.UndefinedColumn:
        print("Таких колон не существует!")
    connection.commit()
elif n == 3:
    table3_name = input("Выберите таблицу: ")
    st_inp = input("Введите id которого нужно удалить: ")
    query3 = f"DELETE FROM {table3_name} WHERE id = {st_inp};"
    try:
        cursor.execute(query3)
        print("Запись успешно удалена!")
    except psycopg2.errors.UndefinedTable:
        print("Такой таблицы не существует!")
    connection.commit()
elif n == 4:
    trun_table_name = input("Какую таблицу хотите очистить?: ")
    query4 = f"TRUNCATE TABLE {trun_table_name}"
    try:
        cursor.execute(query4)
        print(f"{trun_table_name} очищена")
    except psycopg2.errors.UndefinedTable:
        print("Такого файла не сущевствует!!!")
    connection.commit()
elif n == 7:
    cursor.close()
    connection.close()
elif  n == 5:
    table_name = input("Введите название таблицы: ")

    column1 = str(input("Введите колоны:")).split(",")

    query = f"CREATE TABLE {table_name}(id SERIAL PRIMARY KEY,{column1[0]}, {column1[1]}, {column1[2]});"
    try:
        cursor.execute(query)
        print("Успешно создана таблица!")
    except psycopg2.errors.DuplicateTable:
        print("Уже существует такая таблица")
    except psycopg2.errors.SyntaxError:
        print("Колоны введены не правильно")
    except IndexError:
        print("Введите через запятые")
    connection.commit()
elif n == 6:
    table6_name = input("Введите название таблицы: ")
    query6 = f'SELECT * FROM {table6_name};'
    cursor.execute(query6)
    for i in cursor:
        print(i)
else:
    print("Ошибка!")