from twilio.rest import Client 
 
account_sid = 'AC4107dc143bfc240213e67f779e703ce2' 
auth_token = '3d2b20168200dfcbc363d55af9186034' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG05d664871f4c94eef7ebc4524fdb736d', 
                              body='Hello from me, Farzan',      
                              to='+15195891234' 
                          ) 
 
print(message.sid)
