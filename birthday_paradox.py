#How many people do you think it would take to survey, on average, to find two people who share the same birthday? Due to probability, sometimes an event is more likely to occur than we believe it to. In this case, if you survey a random group of just 23 people there is actually about a 50–50 chance that two of them will have the same birthday. This is known as the birthday paradox.

import random
import datetime


birthday=[]
birthday1=[]
i=0
while(i<40):
  year =random.randint(1895,2017)
  #oldeest person ever was 122 years old
  if(year%400==0 or year%4==0 and year%100!=0):
    leap=1
  else:
    leap=0

  month=random.randint(1,12)
  if(month==2 and leap==1):
    day=random.randint(1,29)
  elif(month==2 and leap==0):
    day=random.randint(1,28)
  elif(month==7 or month==8):
    day=random.randint(1,31)
  elif(month%2!=0 and month<7):
    day=random.randint(1,31)
  elif(month%2==0 and month>7 and month<12):
    day=random.randint(1,31)
  else:
    day=random.randint(1,30)

  dd = datetime.date(year,month,day)
  day_of_year=dd.timetuple().tm_yday
  i=i+1
  birthday.append(day_of_year)
  birthday1.append(dd)


birthday.sort()
birthday1.sort()

i=0
while(i<40):
  print(birthday[i])
  print(birthday1[i])
  i=i+1
    
