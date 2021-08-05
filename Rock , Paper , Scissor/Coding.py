def computer():
  import random
  string='RPS'
  x=random.choice(string)
  return x
print('ROCK , PAPER & SCISSOR')
print('RULES..')
print('ROCK + ROCK = DRAW\nROCK + PAPER = PAPER WIN\nROCK + SCISSOR = ROCK WIN')
print('PAPER + PAPER = DRAW\nPAER + SCISSOR = SCISSOR WIN')
print('SCISSOR + SCISSOR = DRAW\n')
choice=input('Enter your choice(R,P,S):- ')

x=computer()
print('Computer Choice:- ',x) 
if choice==(x):
    print('DRAW')
elif choice=='R' and x=='P':
    print('COMPUTER WON')
elif choice=='R' and x=='S':
    print('USER WON')
elif choice=='P' and x=='S':
    print('COMPUTER WON')
elif choice=='P' and x=='R':
    print('USER WON')
elif choice=='S' and x=='R':
    print('COMPUTER WON')
elif choice=='S' and x=='P':
    print('USER WON')
else:
    print('INVALID INPUT')
     

