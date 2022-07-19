import psycopg2
params = f"host={'localhost'} dbname={'itc'} user={'postgres'} password={'1'}"

conn = psycopg2.connect(params)
cursor = conn.cursor()

query = 'CREATE TABLE users4(id SERIAL PRIMARY KEY, name TEXT, last_name TEXT);'

cursor.execute(query)
conn.commit()
cursor.close()
conn.close()