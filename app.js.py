import sqlite3 as sql
# connect to the data_base return connection object
conn = sql.connect('icici_db.db')
cursor_object = conn.cursor()
#==== these are common to dabase creating ======
cursor_object.execute('create table if not exists account(idno integer primary key ,name text ,amount real )')
conn.commit()
#print('db is created ')
pin = int(input('enter ur pin nuber'))
name = input('enter ur name')
amount = int(input('enter ur Amount'))
cursor_object.execute('insert into account values(?,?,?)',(pin,name,amount))
conn.commit()
print('account is created')
conn.close()
print(name ,'thank you')


