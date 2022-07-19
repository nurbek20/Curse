# if name == 1:
    # cursor = conn.cursor()
    # cursor.execute(query)
    # date = cursor.fetchall()
    # print(date)
 # table_name =input("Введите имя автора : ").title()
    # query1 = f"SELECT * FROM author JOIN book  ON book.author_id=author.id JOIN spouse  ON book.author_id=spouse.author_id WHERE author.name = '{table_name}'"
    # cursor.execute(query1)
    # conn.commit()
    # date = cursor.fetchone()
    # print(date)
    # query = 'select name from author;'
    # cursor.execute(query)
    # product = []
    # for i in cursor:    
    # product.append(*i)
    # print(*product)
    # name = str(input("Введите имя писателя:")).title()
    # if name in product:    
    # birth_year = f"Select birth_year from author Where name='{name}'"    
    # cursor.execute(birth_year)    
    # connect.commit()    
    # birth_year_author = cursor.fetchone()    
    # authors_id = f"Select id from author Where name ='{name}'"    
    # cursor.execute(authors_id)    
    # connect.commit() 
     # author_id = cursor.fetchone()    
    # wipe = f"Select name from spouse Where author_id={author_id[0]}"    
    # cursor.execute(wipe)    
    # connect.commit()
     # authors_wipe = cursor.fetchone()    
    # wed = f"Select wed_year from spouse Where author_id='{author_id[0]}'"    
    # cursor.execute(wed)    
    # connect.commit()    
    # wed_year = cursor.fetchone()
    # wed_year = cursor.fetchone()    
    # book = f"Select title, year from book Where author_id='{author_id[0]}'"    
    # cursor.execute(book)    
    # connect.commit()    
    # books = cursor.fetchone()    
    # print(f"""Писатель:{name}
    # Год рождения:{birth_year_author[0]}-год
    # Супруг(а):{authors_wipe[0]}
    # Брак:{wed_year[0]}.
    # Книги:{books[0]}""")
    # else:    
    #   print("В списке нету такого писателя")
# from dsn import connect
    
import psycopg2
connect = psycopg2.connect(
    host = "localhost", 
    port="5432", 
    database="postgres", 
    user="postgres", 
    password="postgres")
query = "SELECT * FROM author;"
cursor.execute(query)
name = []
for i in cursor:    
    name.append(*i)
print(*name)
table_name = str(input("Введите  имя  автора: ")).title() 
if table_name in name:
    year = f"SELECT birth_year FROM author WHERE name = '{table_name}';" 
    cursor.execute(year)    
    connect.commit()
    birth_year = cursor.fetchone()
    author_id = f"SELECT id FROM author WHERE name = '{table_name}';" 
    cursor.execute(author_id)    
    connect.commit()
    author1_id = cursor.fetchone()
    spouse = f"SELECT name FROM spouse WHERE author_id = {author_id[0]};"
    cursor.execute(spouse)    
    connect.commit() 
    author_spouse = cursor.fetchone() 
    wed = f"SELECT wed_year FROM spouse WHERE author_id = '{author_id[0]}';"
    cursor.execute(wed)    
    connect.commit()    
    wed_year = cursor.fetchone()  
    book = f"SELECT title, year FROM book WHERE author_id = '{author_id[0]}';" 
    cursor.execute(book)
    connect.commit()
    books = cursor.fetchone()
    print(f"""Писатель: {name}
    Год рождения: {birth_year[0]} - год
    Супруг(а): {author1_id}.
    Брак: {wed_year[0]}.
    Книги: {books[0]}""") 
else:
    print("В списке нету такого писателя")  
