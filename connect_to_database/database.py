import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd='abgk1234',database="school")
mycursor=mydb.cursor()
mycursor.execute("select * from s_d")
for i in mycursor:
    print(i)
