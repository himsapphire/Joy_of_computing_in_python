""" Here, we took a file containg a binary string(representing our DNA), then we tried evoluting the dna, such that we are randomly choosing an index from the string and thwn with equal probability we are changing that bit(if 0) to bit=1."""
import random


def evolve(x):
  #generating index of variable
  ind=random.randint(0,len(x)-1)
  #to change bit at x or not depends on p
  #if p==1 then change the bit at ind index of list 
  p=random.randint(1,100)
  if(p==1):
    print(ind)
    if(x[ind]=='0'):
      x[ind]='1'
    else:
      x[ind]='0'
    
#opening our file having gene constitution
with open("file.txt.txt","r+") as myfile:
  x=myfile.read()
  #file is read and kept as string in x
  #converting it to a list
  x=list(x)
for i in range(0,len(x)):
  evolve(x)
print(x)  
myfile.close()
