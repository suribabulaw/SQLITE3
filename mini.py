import sqlite3 as sql
#===============bsbs============
min_t = sql.connect('min_st.db')
min_c= min_t.cursor()
min_c.execute('create table mini_statement(pin integer ,amount_d real ,amout_w real )')
################
conn = sql.connect('icici_db.db')
cursor_object = conn.cursor()
pin = int(input('enter ur pin number'))
surh = cursor_object.execute('select * from account where idno = ?',(pin,))
#print(surh.fetchone())
res = surh.fetchone()



