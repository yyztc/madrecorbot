import sys
import pymssql
import platform
import config

print(platform.platform())

conn = pymssql.connect(
    server="{}",
    database="{}", 
    user="{}",
    password="{}").format(config.rmServer, config.rmDB, config.rmUser, config.rmPss)

cur = conn.cursor()
cur.execute('SELECT * FROM GUSUARIO')

class rmConnection:
    
    def __init__(self , name = '', user = ''):

        self.name = name
        self.user = user
        for row in cur:
            if str.lower(row[1]) == str.lower(self.name) or str.lower(row[0]) == str.lower(self.user):
                self.row = row
    
    def getUser(self):
        return self.row[0]

    def getActivateUser(self):
        return self.row[2]
    
    def getAllSchema(self):
        return self.row
    
    def getName(self):
        return self.row[1]

#print(rmConnection(name='Raphael Miranda Rezende').getAllSchema())
