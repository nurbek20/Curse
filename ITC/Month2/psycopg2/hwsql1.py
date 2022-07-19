import psycopg2

conn = psycopg2.connect(host= "localhost", 
    port="5432", 
    database="postgres", 
    user="postgres", 
    password="postgres")
# print("Успешно подключено к базе данных")

while True:
    n=int(input("""Для создания новую таблицы введите 1:
Для записи введите 2:
Если хотите изменить столбца введите 3: 
Если хотите удалить запись введите 4:
Если хотите очистить таблицу введите 5:
Чтобы Открыть таблицу введите 6:
Если хотите удалить таблицу введите 7
Для выхода введите 8: """))
    if  n == 1:
        cursor = conn.cursor()
        table_name = input("Введите называние таблицы: ")
    
        column1 = str(input("Введите колоны: ")).split(",")
    
        query = f"CREATE TABLE {table_name}(id SERIAL PRIMARY KEY,{column1[0]} , {column1[1]} , {column1[2]} );"
        try:
            print("Успешно создана таблица!")
        except psycopg2.errors.DuplicateTable:
            print("Уже существует такая таблица")
        except psycopg2.errors.SyntaxError:
            print("Колоны введены не правильно")
        except IndexError:
            print("Введите через запятые")
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    elif n == 2:
        cursor = conn.cursor()
        table1_name = input("Выберите таблицу: ")
        COLUMNS = input("Введите колоны через запятые: ").split(",")
        VALUES1 = input("Введите записи через запятые: ").split(",")
        query1 = f"INSERT INTO {table1_name}({COLUMNS[0]}, {COLUMNS[1]}, {COLUMNS[2]}) VALUES('{VALUES1[0]}', '{VALUES1[1]}', '{VALUES1[2]}');"
        try:
            cursor.execute(query1)
            print("Запись успешно добавлена!!!")
        except psycopg2.errors.UndefinedTable:
            print("Такой таблицы не существует!")
        except psycopg2.errors.UndefinedColumn:
            print("Таких колон не существует!")
        conn.commit()  
    elif n == 3:
        cursor = conn.cursor()
        table2_name = input("Выберите таблицу: ")
        f_inp = input("Введите называние столбца: ")
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
        conn.commit() 
    elif n == 4:
        cursor = conn.cursor()
        table3_name = input("Выберите таблицу: ")
        st_inp = input("Введите id которого нужно удалить: ")
        query3 = f"DELETE FROM {table3_name} WHERE id = {st_inp};"
        try:
            cursor.execute(query3)
            print("Запись успешно удалена!")
        except psycopg2.errors.UndefinedTable:
            print("Такой таблицы не существует!")
        conn.commit()     
    elif n == 5:
        cursor = conn.cursor()
        trun_table_name = input("Какую таблицу хотите очистить?: ")
        query4 = f"TRUNCATE TABLE {trun_table_name}"
        try:
            cursor.execute(query4)
            print(f"{trun_table_name} очищена")
        except psycopg2.errors.UndefinedTable:
            print("Такого файла не сущевствует!!!")
        conn.commit()
    elif n == 6:
        table6_name = input("Введите название таблицы: ")
        cursor = conn.cursor()
        try:
            query6 = f'SELECT * FROM {table6_name};'
            print(f"{table6_name}")
        except psycopg2.errors.UndefinedTable:
            print("Такого таблица не сущевствует!!!")    
        cursor.execute(query6)
        date = cursor.fetchall()    
        print(date)
    elif n == 7:
        cursor = conn.cursor()
        table7_name = input("Введите называние таблицы: ")
        query7 = f"DROP TABLE {table7_name};"
        try:
            print("Таблица удалень")
        except psycopg2.errors.UndefinedTable:
            print("Такого таблица не сущевствует!!!")
        cursor.execute(query7)      
        conn.commit()
        cursor.close()
        conn.close()
    elif n == 8:
        quit()
else:
        print("Ошибка!")