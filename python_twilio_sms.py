from query_fetch_all import query_with_fetchall
from twilio.rest import Client

array_numbers = query_with_fetchall()

def twilio_api_sms():
                global array_numbers
                body_input = input('Type the message body:')
#                twilioconfig = read_twilio_config()
                account_sid = 'AC73b99b46f6fabe9ab60147ed45b58215'
                auth_token = 'cee21593cdd05684ed6027bfd2b94a24'
                client = Client(account_sid, auth_token)
                for number in array_numbers:
                        message = client.messages.create(
                               from_='15107565042',
                               body=body_input,
                               to=number
                          )
                print(message.sid)

if __name__ == '__main__':
	twilio_api_sms()	
