import psycopg2
import sys
import time
import config
#import newAD

conn = psycopg2.connect(
    host="{}",
    database="{}", 
    user="{}",
    password="{}",
    port="{}").format(config.herokuHost, config.herokuDB, config.herokuUser, config.herokuPss, config.herokuPort)

cur = conn.cursor()

print('PostgreSQL connection at https://madrecorbot.herokuapp.com/' )

def insertIntoCreatedUser(name, user, sector):
    cur.execute('INSERT INTO createdUser(nome, usuario, setor) VALUES(%s, %s, %s)', [name, user, sector])
    conn.commit()

def getMaxCreated():
    aL = cur.execute('SELECT max(id) FROM createdUser')
    aLL = cur.fetchall()[0]
    return aLL

def getMaxCreate():
    aL = cur.execute('SELECT max(id) FROM createUser')
    aLL = cur.fetchall()[0]
    return aLL

def getCreatedSchema():
    aL = cur.execute('SELECT max(id) FROM createdUser')
    aLL = cur.fetchall()[0]
    last = cur.execute('SELECT * FROM createUser WHERE id=%s', [aLL])
    #print(cur.fetchall()[0])
    return cur.fetchall()

def getCreateSchema():
    aL = cur.execute('SELECT max(id) FROM createUser')
    aLL = cur.fetchall()[0]
    last = cur.execute('SELECT * FROM createUser WHERE id=%s', [aLL])
    #print(cur.fetchall()[0])
    return cur.fetchall()

print('''
 __  __           _                         ____   ____ _______ 
|  \/  |         | |                       |  _ \ / __ \__   __|
| \  / | __ _  __| |_ __ ___  ___ ___  _ __| |_) | |  | | | |   
| |\/| |/ _` |/ _` | '__/ _ \/ __/ _ \| '__|  _ <| |  | | | |   
| |  | | (_| | (_| | | |  __/ (_| (_) | |  | |_) | |__| | | |   
|_|  |_|\__,_|\__,_|_|  \___|\___\___/|_|  |____/ \____/  |_|   


''')

while True:

    create = getCreateSchema() #Pegar último usuário a ser criado
    created = getCreatedSchema() #Pegar último usuário que foi criado
    if create[1] != created[1]:
        newAD.createUser(create[1], create[2], create[3]) #Criar usuário no Active directory e Itop
    print(create)
    print(created)
    time.sleep(30)
    

