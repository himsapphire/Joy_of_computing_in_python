from PIL import Image
import random

end=100
ladder={4:22,14:77,67:82,10:29,33:51,74:90}
snake={95:36,81:78,92:52,50:16,40:20}

def checkladder(point):
  for i in ladder.items():
    if(point==ladder.keys()):
       return ladder.values()
  return point    

def checksnake(point):
  for i in snake.items():
    if(point==snake.keys()):
       return snake.values()      
  return point

def show_board():
  img=Image.open('snake.jpg')
  img.show()
  img.save('snake.jpg')

def play():
  p1name=input("player1, enter your name")
  p2name=input("player2, enter your name")
  pp1=0
  pp2=0

  turn=0
  while(1):
    if(turn%2==0):
      print(p1name,'your turn')
      c=int(input('press 1 to continue, 0 to quit'))
      if(c==0):
        print(p1name, 'your score',pp1)
        print(p2name, 'your score',pp2)
        print('Thanks for playing')
        break

      dice=random.randint(1,6)
      print("number on dice ",dice)
      pp1=pp1+dice
      """check for ladder at this point"""
      show_board()
      pp1=checkladder(pp1)
      pp1=checksnake(pp1)

      print(pp1)
      if(int(pp1)>=end):
        print(p1name," you won ")
        print("your score is ",pp1)
        break;

    else:
      print(p2name,' your turn ')
      c=int(input('press 1 to continue, 0 to quit'))
      if(c==0):
        print(p1name, 'your score',pp1)
        print(p2name, 'your score',pp2)
        print('Thanks for playing')
        break

      dice=random.randint(1,6)
      print("number on dice ",dice)
      pp2=pp2+dice
      """check for ladder at this point"""
      show_board()
      pp2=checkladder(pp2)
      pp2=checksnake(pp2)

      print(pp2)
      if(int(pp2)>=end):
        print(p1name," you won ")
        print("your score is ",pp1)
        break;

    turn=turn+1;
      


show_board()
play()
