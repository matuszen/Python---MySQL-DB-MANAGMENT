from mysql.connector import connect

dbconnect = open('dbconnect.txt', 'r').readlines()

user = (dbconnect[0][5:]).strip()
password = (dbconnect[1][9:]).strip()
host = (dbconnect[2][5:]).strip()
database = (dbconnect[3][9:]).strip()

conn = connect(
    user = user,
    password = password,
    host = host,
    database = database
)

print(f'Połączono z {host}')
print(f'Baza danych: {database}')

while True:
    query = input(f'[{user}@{database}]$ ').strip()

    if query == 'end':
        break

    cursor = conn.cursor()
    cursor.execute(query)

    result = cursor.fetchall()

    for record in result:
        print(record)

    print()

input('\nNacisnij dowolny klawisz aby wyjść z programu')
