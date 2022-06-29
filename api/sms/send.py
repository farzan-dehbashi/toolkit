from twilio.rest import Client 
 
account_sid = 'AC4107dc143bfc240213e67f779e703ce2' 
auth_token = '[79d97bf7985186929b6f1cc8490e14fe]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG05d664871f4c94eef7ebc4524fdb736d', 
                              body='Just my first note',      
                              to='+15195891234' 
                          ) 
 
print(message.sid)