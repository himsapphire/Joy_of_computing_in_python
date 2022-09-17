#Link to the detailed version of the problem - https://statisticsbyjim.com/fun/monty-hall-problem/


import random

door=[0] * 3
goatdoor=[]
swap=0 #no of wins after swapping
no_swap=0 #no of wins after not swapping
j=0
while(j<10):
  x=random.randint(0,2) #xth door that will have BMW
  door[x]="BMW"
  for i in range(3):
    if(i==x):
      continue
    else:
      door[i]="GOAT"
      goatdoor.append(i)

  #1.ask user for its input
  choice=int(input("Enter your choice: "))
  """"  what if you already chose the right 1"""
  #2. Now, he will open a door for user
  #the door wouldnt be the actual door, but a goatdoor
  door_open=random.choice(goatdoor)
  # this door_open shouldnt be equal to door chosen by user
  while choice==door_open:
    door_open=random.choice(goatdoor)
  
  ch=input("do u want to swap? y/n  : ")
  if(ch=='y'):
    if(door[choice]=='GOAT'):
      # and he swapped
      print("\nu won")
      swap=swap+1
    else:
      print("\nu lost")

  else:
    #i.e if he chose to not swap
    if door[choice=='GOAT']:
      print("\nu lost")
    else:
      print("\nu won")
      no_swap=no_swap+1

  j=j+1

print(swap)
print(no_swap)
