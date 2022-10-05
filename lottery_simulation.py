import random
import matplotlib.pyplot as plt


account=0
x=[]
y=[]

for i in range(365):
  x.append(i+1)
  bet=random.randint(1,10)
  lucky_draw=random.randint(1,10)
  print("your bet",bet)
  print("your lucky draw",lucky_draw)
  if bet==lucky_draw:
    account+=900-100
  else:
    account-=100
  y.append(account)

plt.plot(x,y)
plt.show()
#print (account)  
