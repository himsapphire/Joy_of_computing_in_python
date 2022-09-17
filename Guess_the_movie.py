#in the following code, two people are playing, in which one has to guess the movie.
#Firstly, player will try to guess a letter present in it and if present then , ques will unlock accordingly


import random

movies=["udta punjab",'gangubai',"raazi","darlings"]

#create question function
def create_ques(movie):
  n=len(movie)
  letters=list(movie)
  temp=[]
  for i in range(n):
    if(letters[i]==' '):
      temp.append(" ")
    else:
      temp.append("*")

  qn=''.join(str(x) for x in temp)
  return qn


#if letter is present in function
def is_present(letter,movie):
  c=movie.count(letter)
  if(c==0):
    return False
  else:
    return True


#unlock function
def unlock(qn,movie,letter):
  m=list(movie)
  q=list(qn)
  temp=[]
  n=len(movie)
  for i in range(n):
    if(m[i]==letter):
      temp.append(letter)
    else:
      temp.append(q[i])

  new_q=''.join(str(x) for x in temp)
  return new_q
    

def play():
  print("To make it easy for you to guess , movies are of 'Alia Bhatt'\n")
  p1name=input("player 1, Enter your name : ")
  print("\n")
  p2name=input("Player 2,Enter your name : ")
  print("\n")
  s1=0
  s2=0
  turn=0
  willing=True
  while willing:
    if turn%2==0:
      #player 1
      print(p1name," : your turn \n")
      picked_movie=random.choice(movies)

      #firstly the question would just appears as blanks or stars
      qn=create_ques(picked_movie)
      modified_qn=qn
      print("Here is the question",qn)

      #player1 will keep guessing the movie until he gets it right
      not_said=True
      while not_said:
        letter=input("\n Guess a letter that may be in the movie : ")
        #ifletter is present in the movie
        if(is_present(letter,picked_movie)):
          #unlock
          modified_qn=unlock(modified_qn,picked_movie,letter)
          print("\n",modified_qn)
          d=int(input("Press 1 to guess or 2 to continue : "))
          if(d==1):
            ans=input("\nyour guess : ")
            if(ans==picked_movie):
              s1=s1+1
              print("\nyour answer is correct and your score is: ",s1)
              not_said=False
            else:
              print("wrong answer, try again \n")
                
        else:
          print(letter, " is not in the movie , try to guess letter again. \n")


      # now, that player 1 has played his part ask if he wants to continue or endgame
      c=int(input("\nenter 1 if you wanna continue game or 0 to quit : ")) 
      if(c==0):
        willing=False
        print(p1name," \nyour score : ",s1)
        print(p2name," your score : ",s2)
        print("thanks for playing u guys..\n")

    else:
      #player2
      print(p2name," : your turn\n")
      picked_movie=random.choice(movies)

      #firstly the question would just appears as blanks or stars
      qn=create_ques(picked_movie)
      modified_qn=qn
      print(qn)

      #player2 will keep guessing the movie until he gets it right
      not_said=True
      while not_said:
        letter=input("\n Guess a letter that maybe in the movie : ")
        if(is_present(letter,picked_movie)):
          #unlock
          modified_qn=unlock(modified_qn,picked_movie,letter)
          print("\n",modified_qn)
          d=int(input("Press 1 to guess or 2 to continue : "))
          if(d==1):
            ans=input("\nyour answer : ")
            if(ans==picked_movie):
              s2=s2+1
              print("\nyour answer is correct and your score is: ",s1)
              not_said=False
            else:
              print("\nwrong answer, try again \n")
                
        else:
          print(letter, " is not in the movie , try to guess letter again. \n")


      # now, that player 2 has played his part ask if he wants to continue or endgame
      c=int(input("\nenter 1 if you wanna continue game or 0 to quit : ")) 
      if(c==0):
        willing=False
        print(p1name," \nyour score : ",s1)
        print(p2name," your score : ",s2)
        print("thanks for playing u guys..\n")

    turn=turn+1  

play()
