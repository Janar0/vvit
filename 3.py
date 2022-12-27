import sqlite3
#create a database with name mtuci_db
conn = sqlite3.connect('mtuci_db.db')
c = conn.cursor()
#create new table with name 'mtuci_db',  REFERENCES name connected to chairs and name
c.execute('''CREATE TABLE mtuci_db
                (id integer, name text, chair text, FOREIGN KEY (chair) REFERENCES chairs(name))''')
#insert data to table
c.execute("INSERT INTO mtuci_db VALUES (1, 'Бин2202', 'Сисс')")
c.execute("INSERT INTO mtuci_db VALUES (2, 'Бин2203', 'Сисс')")
c.execute("INSERT INTO mtuci_db VALUES (3, 'БиБ2204', 'Мтс')")
#create new table with name 'chairs',  REFERENCES id connected to mtuci_db and name
c.execute('''CREATE TABLE IF NOT EXISTS chairs
                (id integer, name text)''')

c.execute("INSERT INTO chairs VALUES (1, 'Сисс')")

c.execute("INSERT INTO chairs VALUES (2, 'Мтс')")
#create new table with name 'students', id,  REFERENCES name connected to mtuci_db and integer passport
c.execute('''CREATE TABLE IF NOT EXISTS students
                (id integer, name text, passport integer, FOREIGN KEY(name) REFERENCES mtuci_db(name))''')

c.execute("INSERT INTO students VALUES (1, 'Бин2202', 123456)")

c.execute("INSERT INTO students VALUES (2, 'Бин2203', 12342346)")

c.execute("INSERT INTO students VALUES (3, 'БиБ2204', 123213432)")

for row in c.execute('SELECT * FROM students'):
    print(row)

conn.close()


