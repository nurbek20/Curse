import psycopg2

connection = psycopg2.connect(host="localhost", port="5432", dbname="ITC",user="postgres", password=input("Введите ваш пароль: "))

cursor = connection.cursor()

query = "CREATE TABLE book_new(id SERIAL PRIMARY KEY, title VARCHAR(50), author VARCHAR(100), genre VARCHAR(30));"

# try:
#     cursor.execute(query)
#     print("Успешно создана таблица!")
# except psycopg2.errors.DuplicateTable:
#     print("Уже существует такая таблица")

VALUES1 = input("title")
VALUES2 = input("author")
VALUES3 = input("genre")
query2 = f"INSERT INTO book_new(title, author, genre) VALUES('{VALUES1}', '{VALUES2}', '{VALUES3}')"

query2 = "INSERT INTO book_new(title, author, genre) VALUES('book', 'test', 'test');"
cursor.execute(query2)

connection.commit()
cursor.close()
connection.close()