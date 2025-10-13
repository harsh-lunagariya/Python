import mysql.connector

try:
    myDB = mysql.connector.connect(
        host="localhost",  # Or the IP address/hostname of your MySQL server
        user="mysql",
        password="root"
    )

    if myDB.is_connected():
        print("Connected to MySQL database successfully!")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

myCursor = myDB.cursor()

myCursor.execute("show databases;")
print()

for i in myCursor:
    for j in i:
        print(f"{j}     ",end='')
    print()