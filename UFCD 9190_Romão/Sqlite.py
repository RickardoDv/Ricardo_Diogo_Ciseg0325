#SQLite3
import sqlite3
nomeBD="BaseDeDados.db"
global conn
conn=sqlite3.connect(nomeBD)
c = conn.cursor()
sql="""
create table helldivers (
    id integer primary key autoincrement not null,
    username text not null,
    password text not null
);
"""
try:
    conn.executescript(sql)
    conn.commit()
except:
    print("A tabela já existe")

#inserir dados para a bd

username= input("Inserir Username: ")
password= input("Inserir Password: ")

#Metodo Incorreto
#sql= "INSERT INTO helldivers (username, password) VALUES ('" + username + "', '" + password + "');"

#conn.executescript(sql)
#conn.commit()

sql= "INSERT INTO helldivers (username, password) VALUES (?,?);"

dados=(username,password)
c.execute(sql, dados)
conn.commit()

sql="SELECT * FROM helldivers;"
c.execute(sql)
resultado=c.fetchall()

for registo in resultado:
    print(registo[2])