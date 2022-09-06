#datetime_library in python

import datetime
import pytz

#today's date
print(datetime.date.today())
#print just current year
print(datetime.date.today().strftime("%Y"))
#current  month
print(datetime.date.today().strftime("%B"))
#current week of the year
print(datetime.date.today().strftime("%W"))
#day of week in number
print(datetime.date.today().strftime("%w"))
#today' day number as for a year
print(datetime.date.today().strftime("%j"))
#day of week in words
print(datetime.date.today().strftime("%A"))
#current time in Greenwich
print(datetime.datetime.now())
#current time acc to timezone      
print(datetime.datetime.now(pytz.timezone("Asia/Kolkata")))
