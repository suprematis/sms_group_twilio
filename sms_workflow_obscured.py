from twilio.rest import Client 
import csv

with open('numbers.csv') as csv_numbers:
	csv_reader = csv.reader(csv_numbers, delimiter=',')
	array_num = []
	for row in csv_reader:
#		print('{}'.format(row[0]))
		array_num.append(row[0])
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
