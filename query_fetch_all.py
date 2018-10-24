from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
#from python_twilio_apiconfig import read_twilio_config
#import csv

def query_with_fetchall():
	try:
		dbconfig = read_db_config()
		array_num = []
		conn = MySQLConnection(**dbconfig)
		cursor = conn.cursor()
# Narrowed SQL query to one number for specific purposes.	
		cursor.execute("SELECT phone FROM address WHERE phone IN ('+19259614345','+19252346209');")
		rows = cursor.fetchall()
		for row in rows:
			array_num.append(row[0])
		print(array_num)
		return array_num
	except Error as e:
		print(e)

	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	query_with_fetchall()
