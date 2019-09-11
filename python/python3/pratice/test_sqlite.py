# -*- coding: utf-8 -*-
import os
import sqlite3


database_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(database_file):
    os.remove(database_file)

# init database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()
cursor.execute(
    'CREATE TABLE user(id varchar(20) primary key, name varchar(20))'
    )
cursor.execute('INSERT INTO user(id, name) values ("1", "haibao")')
cursor.rowcount
cursor.close()
conn.commit()
conn.close()

# search sqlite object
conn = sqlite3.connect(database_file)
cursor = conn.cursor()
cursor.execute('SELECT * FROM user where id="1"')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
