import sqlite3 as sql
conn = sql.connect('icici_db.db')
cursor_object = conn.cursor()
################################################################
pin = int(input('enter ur pin number'))
surh = cursor_object.execute('select * from account where idno = ?',(pin,))
#print(surh.fetchone())
res = surh.fetchone()

if res == None:
    print(' pin is increat')
else:
    w_money = int(input('enter amout to with draw'))
    if w_money %100 != 0 :
        print('matliple == 100')
    else:
        #print('100')
        if w_money > 50000 :
            print('plz inter less than 50000')
        else:
             if w_money > res[2]:
                print('not founds ur account')
             else:
                 w_mount = res[2]-w_money
                 cursor_object.execute('update account set amount = ? where idno= ?',(w_mount,pin))
                 conn.commit()
                 after = cursor_object.execute('select * from account where idno = ?' ,(pin,))
                 naik=after.fetchone()
            # print(naik[2])
                 print("thanku ur traction seccus")
                 print('in place is ', naik[2])
                 print('thank you naveen ====')

