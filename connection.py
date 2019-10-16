import psycopg2
import sys
from rmConected import *
import config

conn = psycopg2.connect(
    host="{}",
    database="{}", 
    user="{}",
    password="{}",
    port="{}").format(config.herokuHost, config.herokuDB, config.herokuUser, config.herokuPss, config.herokuPort)

cur = conn.cursor()

print('PostgreSQL connection at https://madrecorbot.herokuapp.com/' )

#cur.execute('CREATE TABLE createUser(id SERIAL PRIMARY KEY,nome VARCHAR(200), usuario VARCHAR(50), setor VARCHAR(50))')
#cur.execute('CREATE TABLE createdUser(id SERIAL PRIMARY KEY,nome VARCHAR(200), usuario VARCHAR(50), setor VARCHAR(50))')
#cur.execute('DELETE FROM createdUser')
#cur.execute('DELETE FROM createUser')
#clearconn.commit()

def insertIntoCreateUser(name, user, sector):
    cur.execute('INSERT INTO createUser(nome, usuario, setor) VALUES(%s, %s, %s)', [name, user, sector])
    conn.commit()

def insertIntoCreatedUser(name, user, sector):
    cur.execute('INSERT INTO createdUser(nome, usuario, setor) VALUES(%s, %s, %s)', [name, user, sector])
    conn.commit()

def getCreatedSchema():
    cur.execute('SELECT * FROM createdUser')
    #print(cur.fetchall())
    t = cur.fetchall()
    for row in t:
        print(row)

def deleteAll():
    cur.execute('DELETE FROM createdUser')
    conn.commit()
    cur.execute('DELETE FROM createUser')
    conn.commit()
    #print(cur.fetchall())
    #t = cur.fetchall()
    #for row in t:
    #    print(row)

def getCreateSchema():
    cur.execute('SELECT * FROM createUser')
    #print(cur.fetchall())
    t = cur.fetchall()
    for row in t:
        print(row)

#insertIntoCreatedUser('desbugar', 'desbug', 'desbugger')

while True:

    print('''
 __  __           _                         ____   ____ _______ 
|  \/  |         | |                       |  _ \ / __ \__   __|
| \  / | __ _  __| |_ __ ___  ___ ___  _ __| |_) | |  | | | |   
| |\/| |/ _` |/ _` | '__/ _ \/ __/ _ \| '__|  _ <| |  | | | |   
| |  | | (_| | (_| | | |  __/ (_| (_) | |  | |_) | |__| | | |   
|_|  |_|\__,_|\__,_|_|  \___|\___\___/|_|  |____/ \____/  |_|   

    ''')

    getI = int(input('''
1 - Criar usuário
2 - Mostrar usuários criados
3 - Mostrar usuários a serem criados
4 - Deletar todos usuários
0 - Exit
'''))

    if getI == 0:
        sys.exit()
    elif getI == 1:
        getAll = input('Digite nome e setor do usuário novo: ').split(', ')
        print(getAll)
        user = rmConnection(name=getAll[0]).getUser()
        print(user)
        insertIntoCreateUser(getAll[0], user, getAll[1])
    elif getI == 2:
        getCreatedSchema()
    elif getI == 3:
        getCreateSchema()
    elif getI == 4:
        deleteAll()