from datetime import datetime
from datetime import time

now = datetime.now() # time object
print('date and time=', now)
now = datetime.now().time()
print("time =", now)

time1 = time(0, 0, 12) #makes an object with 12 seconds length
print(time1)

time2 = datetime()
#now.microsecond
#now.second
#now.hour
#now.minute
