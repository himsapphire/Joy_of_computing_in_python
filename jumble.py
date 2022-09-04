""" In this game there are two players, computer will through a jumbled question to the player and the player had to answer it accordingly
"""

import random

def choose():
    words=['rainbow','computer','sonali','utkalika']
    #randomly picks a word from list
    pick=random.choice(words)
    return pick

def jumble(word):
    #choosing some letters(here the whole length) from a given word in any order
    jumbled_word="".join(random.sample(word,len(word)))
    return jumbled_word

def thank(p1n,p2n,s1,s2):
    print(p1n,'your score is',s1)
    print(p2n,'your score is',s2)
    print('thanks for playing')

def play():
  p1name=input("player 1, enter your name : ")
  p2name=input("player2, enter your name : ")
  s1=0
  s2=0
  turn=0
  while(1):
    #computer's task
    picked_word=choose()
    #create question
    qn=jumble(picked_word)
    print('here,take ur question : ',qn)
    if turn%2 ==0:
      print(p1name,' , your turn')
      ans=input('give your answer : ')
      if(ans==picked_word):
        s1=s1+1
        print('your score : ',s1)
      else:
        print('you got it wrong, the word was: ',picked_word)
      c=int(input('press 1 to continue and 0 to quit : '))
      if(c==0):
        thank(p1name,p2name,s1,s2)
        break
                
    else:
      print(p2name,'your turn ')
      ans=input('give your answer : ')
      if(ans==picked_word):
        s2=s2+1
        print('your score : ',s2)
      else:
        print('you got it wrong, the word was : ',picked_word)
      c=int(input('press 1 to continue and 0 to quit : '))
      if(c==0):
        thank(p1name,p2name,s1,s2)
        break
    turn=turn+1
        
play()
