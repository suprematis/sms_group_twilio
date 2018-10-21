# Python code to demonstrate SQL to fetch data. 
  
# importing the module 
#import mysql.connector
from mysql.connector import MySQLConnection, Error 
 
# connect withe the myTable database 
mysql.connector.connect(host='192.168.86.115',database='viking',user='root',password='As032484?') 

def query_with_fetchone():
    try:
       # dbconfig = read_db_config()
       # conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM staff")
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchone()
