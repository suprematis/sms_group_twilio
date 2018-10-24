from python_mysql_dbconfig import read_db_config
from python_twilio_apiconfig import read_twilio_config
from twilio.rest import Client

twilioconfig = read_twilio_config()
twilioargs = Client(*twilioconfig)
dbconfig = read_db_config()
print(dbconfig)
