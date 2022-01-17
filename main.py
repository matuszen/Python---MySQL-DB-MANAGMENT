import mysql.connector

dbconnect = open('dbconnect.txt', 'r').readlines()

user = (dbconnect[0][5:]).strip()
password = (dbconnect[1][9:]).strip()
host = (dbconnect[2][5:]).strip()
database = (dbconnect[3][9:]).strip()

conn = mysql.connector.connect(

    user=user,
    password=password,
    host=host,
    database=database

)

print('Połączono z', host)
print('Baza danych:', database)

while True:
    query = input('>>>').strip()

    if query == 'end':
        break

    cursor = conn.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    for record in result:
        print(record)

    print()

input('\nNacisnij dowolny klawisz aby wyjść z programu')
