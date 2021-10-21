import mysql.connector
while True:
    name = input("Enter you name: ")
    age = input("Enter age: ")
    if age.isalnum():
        break
    print("Enter correct value")
while True:
    password = input("Select a new password: (only alphabets and numbers)")
    if password.isalnum():
        break
    print("Password can only contain letters and numbers")
