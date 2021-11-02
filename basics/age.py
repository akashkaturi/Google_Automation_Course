import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="8341415122")
mycursor=mydb.cursor()
for i in mycursor:
    print(i)
# while True:
#     name = input("Enter
# you name: ")
#     age = input("Enter age: ")
#     if age.isalnum():
#         break
#     print("Enter correct value")
# while True:
#     password = input("Select a new password: (only alphabets and numbers)")
#     if password.isalnum():
#         break
#     print("Password can only contain letters and numbers")


