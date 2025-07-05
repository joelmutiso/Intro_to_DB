import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="123Joewonderventures@", 
        database="company_bd" 
)
    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except Error:
    print(f"except mysql.connector.Error")
finally:
    try:
        if cursor:
            cursor.close()
        if mydb.is_secure:
                mydb.close()
    except:
        pass