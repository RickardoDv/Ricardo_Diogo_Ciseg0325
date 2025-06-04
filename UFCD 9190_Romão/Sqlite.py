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

conn.executescript(sql)
conn.commit()

