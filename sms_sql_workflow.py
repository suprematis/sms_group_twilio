from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from twilio.rest import Client 
#import csv

def query_with_fetchall():
	try:
		dbconfig = read_db_config()
		array_num = []
		conn = MySQLConnection(**dbconfig)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM address WHERE phone LIKE '+19252346209'")
		rows = cursor.fetchall()
#       print('Total Row(s):', cursor.rowcount)
		for row in rows:
#            print(row[6])
			array_num.append(row[6])

		body_input=input('Type the message body:')
		account_sid = 'AC73b99b46f6fabe9ab60147ed45b58215'
		auth_token = 'cee21593cdd05684ed6027bfd2b94a24'
		client = Client(account_sid, auth_token)
		for number in array_num:
        		message = client.messages.create(
                                from_='15107565042',
                                body=body_input,
                                to=number
                          )
		print(message.sid)

	except Error as e:
		print(e)

	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	query_with_fetchall()
