import sqlite3 as sql
conn = sql.connect('icici_db.db')
cursor_object = conn.cursor()
pin = int(input('enter ur pin number'))
surh = cursor_object.execute('select * from account where idno = ?',(pin,))
#print(surh.fetchone())
res = surh.fetchone()

if res == None:
    print(' pin is increat')
else:
    print('1) ur account info')
    print('2)withdraw money')
    print('3)view balence ')
    print('4) deposite money')
    print('5 pin change')
    option = int(input('inter operation'))
    if option > 6 :
        print('valid nubrtrt')
    elif option == 1:
        print('ur pin nuber is' , res[0])
        print('name ' , res[1])
        print('available balence is ' , res[2])
    elif option == 2:

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
                     print('thank you ',naik[1],' ====')
    elif option == 3:
        print('view balence')
    elif option == 4:
        D_amount =int(input('enter amount to deposite '))
        if D_amount%100 != 0 :
            print('plze valid amout with malti 100')
        else:
            cur_am_d=res[2]+D_amount
            cursor_object.execute('update account set amount = ? where idno = ?',(cur_am_d,pin))
            conn.commit()
            res_d=cursor_object.execute('select * from account where idno =?',(pin,))
            d_reslt=res_d.fetchone()
            print('ur taraction is succssertfdfkfull')
            print('ur avalable balence is',d_reslt[2])

    elif option == 5:

        new_pin1=int(input('enter ur new pin'))
        new_pin2=int(input('reenter new pin'))
        new_pin = new_pin2
        if new_pin1 != new_pin2 :
            print('ur pin not mach')
            print('retry again bye')
        else:

           cursor_object.execute('update account set idno = ? where idno = ?',(new_pin, pin,))
           conn.commit()
           res_d1 = cursor_object.execute('select * from account where idno =?', (new_pin,))
           d_reslt1 = res_d1.fetchone()
           print('ur new pin is', d_reslt1[0])
    else:
        print('plz contact to the nearset atm')





    #
    # w_money = int(input('enter amout to with draw'))
    # if w_money %100 != 0 :
    #     print('matliple == 100')
    # else:
    #     #print('100')
    #     if w_money > 50000 :
    #         print('plz inter less than 50000')
    #     else:
    #          if w_money > res[2]:
    #             print('not founds ur account')
    #          else:
    #              w_mount = res[2]-w_money
    #              cursor_object.execute('update account set amount = ? where idno= ?',(w_mount,pin))
    #              conn.commit()
    #              after = cursor_object.execute('select * from account where idno = ?' ,(pin,))
    #              naik=after.fetchone()
    #         # print(naik[2])
    #              print("thanku ur traction seccus")
    #              print('in place is ', naik[2])
    #              print('thank you naveen ====')
    #

    # # print('1) ur account info')
    # # print('2)withdraw money')
    # # print('5) deposite money') print('5) deposite money')
    # # print('3)view balence ')
    # # print('4)acount balence ')
    # # print('5) deposite money')
    # # print('6 pin change')


# print(res[1])
# print(res[0])
# print(res[2])

