import sqlite3

conn = sqlite3.connect('name1.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER,col_3) ''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES ('name','status','note')''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES ('boat','need repair','boat is broken')''')

cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES ('Teddy Bear ','ok','bear feels well')''')
cursor.execute('''INSERT INTO tab_1(col_1,col_2,col_3) VALUES ('octopus ','broken','felt rather good though had no water to swim')''')
conn.commit()
cursor.execute('''SELECT col_1, col_2, col_3 FROM tab_1''')
k = cursor.fetchall()
print(k)
for i in k:
    e=0
    h=list(i)
    m=' '.join(str(e) for e in h)
    print(m)
