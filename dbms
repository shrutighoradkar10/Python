import mysql.connector
connection=mysql.connector.connect(host='127.0.0.1',database='sbi',user='root',password='root')
mycursor = connection.cursor()
mycursor.execute("create table if not exists bank(username VARCHAR(20),password VARCHAR(20),balance VARCHAR(20),id VARCHAR(20))" )

mycursor = connection.cursor()
n=int(input("1.Register,2.Login:"))
username=""
passwword=""
amount1=""
id=""
if(n==1):
    name=input("Enter Your Name:")
    accno=int(input("Enter Account No:"))
    amount=int(input("Enter Deposit Amount:"))
    pw=input("Enter Your PassWord:")

    username=name
    password=pw
    amount1=amount
    id=accno


    val=(username,password,amount1,id)
    mycursor.execute("create table if not exists bank(username VARCHAR(20),password VARCHAR(20),amount VARCHAR(20),id VARCHAR(20))")

    sql = """INSERT INTO sbi.bank(username, password,balance,id) values (%s,%s,%s,%s)"""
    mycursor=connection.cursor()
    mycursor.execute(sql,val)
    connection.commit()
if(n==2):
    id2=int(input("Enter Your Id:"))
    pas2=input("Enter Your Password:")
    mycursor=connection.cursor()
    mycursor.execute("""select * from sbi.bank where id='%s'"""%(id2))
    row=mycursor.fetchone()
    if mycursor.rowcount==1:

        mycursor.execute("""select * from sbi.bank where password='%s'"""%(pas2))
        row=mycursor.fetchone()
        if mycursor.rowcount==1:
            print("Login Successfully!")
            choice=int(input("Enter 1 for Deposit 2 for Withdrawl 3 for exit:"))
            if choice==1:
                deposit_money=int(input("How much amount You have to deposit?"))
                mycursor.execute("""select balance from sbi.bank where password='%s'"""%(pas2))
                column=mycursor.fetchone()
                x=list(column)
                for i in x:
                    z=int(i)
                    c=z+deposit_money
                mycursor.execute("""update bank  set balance='%s' where password='%s'"""%(c,pas2))

            if choice==2:
                withdraw_money = int(input("How much amount You have to withdraw?"))
                mycursor.execute("""select balance from sbi.bank where password='%s'""" % (pas2))
                column = mycursor.fetchone()
                x = list(column)
                for i in x:
                    z = int(i)
                    c = z - withdraw_money
                mycursor.execute("""update bank  set balance='%s' where password='%s'""" % (c, pas2))
            if choice==3:
                exit(0)
        else:
            print("wrong password!")
    else:
        print("Account Not found!")
    connection.commit()
