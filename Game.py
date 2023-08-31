#Rock Paper Scissors
import sys, random

#Introduction
print ('Welcome  to the Rock, Paper, Scissors game.')
print('Do you want to play this game?')
z=input()
if z != 'yes':
    print('Exiting the program')
    sys.exit()
else:
    print("Let's start the game.")

#mechanics
w=0
l=0
t=0
ai = ('Rock','Paper','Scissors',)
def p():
    return'Paper'
def r():
    return'Rock'
def s():
    return'Scissors'

#Game
while True:
    print(f"{w} Wins, {l} Losses and {t} Ties")
    print('Enter you move: (r)ock, (p)aper, (s)issors or (q)uit. ')
    while True:
        move=input()
        if move=='r' or move=='Rock' or move == 'rock':
            move = r()
            print(f"{move} versus...")
        elif move=='p' or move=='Paper' or move == 'paper':
            move = p()
            print(f"{move} versus...")
        elif move=='s' or move=='scissors' or move == 'Scissors':
            move = s()
            print(f"{move} versus...")
        elif move=='q' or move=='quit' or move=='Quit':
            print('Thanks for playing', end=' ')
            print(f"You played total of {w+l+t} rounds.", end=(' '))
            print(f"Your total score is {w} Wins, {l} Losses and {t} Ties")
            print('Exiting the program')
            sys.exit()
        else:
            print('Enter a valid move')
        if move=='Rock' or move=='Paper' or move=='Scissors':
            break

    m = random.choice(ai)
    print(m)


    if move == m:
            print('Its a tie')
            t=1+t        
    elif move == r() and m == p():
            print('Paper Wins')
            l=1+l
    elif move == r() and m == s():
            print('Rock Wins')
            w=1+w
    elif move == s() and m == r():
            print('Rock Wins')
            l=1+l
    elif move == s() and m == p():
            print('Scissors Wins')
            w=1+w
    elif move == p() and m == r():
            print('Paper Wins')
            w=1+w
    elif move == p() and m == s():
            print('Scissors Wins')
            l=1+l


print(f"Your total score is {w} Wins, {l} Losses and {t} Ties")
print('Thanks for playing', end=' ')