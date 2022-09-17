#program for magic_square, whose elements when summed over a row, or a column or along diagnols gives the same value





def magic_square():
  n=int(input())
  #creating a nxn matrix first
  magic_sq=[]
  for i in range(n):
    l=[]
    for j in range(n):
      l.append(0)
    magic_sq.append(l)  

  #condn 1
  i=n//2
  j=n-1

  num=n*n
  count=1
  
  while(count<=num):
    
    #condn 4
    if(i==-1 and j==n):
      i=0
      j=n-2
    else:
      #if they are differently equal to these values
      #cond2
      
      if(i<0):   #if row exceeding
        i=n-1
        
      if(j>n-1):   #if col exceeding
        j=0
      
      
    if(magic_sq[i][j]==0):
      magic_sq[i][j]=count
      count=count+1
      i=i-1
      j=j+1
    else:
      j=j-2
      i=i+1
    
  
  for i in range(n):
    for j in range(n):
      print(magic_sq[i][j],end=' ')

    print()  

magic_square()

print(n)
