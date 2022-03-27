import os
import time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

###########WIN FLAG##########

Win = 1
Draw = -1
Running = 0
Stop = 1

############################

Game = Running
Mark = 'X'

#Function to draw the Game Board

def DrawBoard():
    print("%c |%c |%c "%(board[1],board[2],board[3]))
    print("__|__|__")
    print("%c |%c |%c "%(board[4],board[5],board[6]))
    print("__|__|__")
    print("%c |%c |%c "%(board[7],board[8],board[9]))
    print("  |  |  ")

#This function check if the position is empty or not

def CheckPosition(x):
    if(board[x]==' '):
        return True
    else:
        return False

#This functions checks player has won or not

def CheckWin():
    global Game

    #horizontal winning condition

    if(board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
        Game = Win
    elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
        Game = Win
    elif(board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
        Game = Win
    #vertical winning condition
    elif(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        Game = Win
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        Game = Win
    elif(board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
        Game = Win
    #diagonal Winning Condition
    elif(board[1]==board[5] and board[5]==board[9] and board[1]!=' '):
        Game = Win
    elif(board[3]==board[5] and board[5]==board[7] and board[3]!=' '):
        Game = Win
    #Match Draw or Tie condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game = Draw
    else:
        Game = Running

#############################################################################

print("TIC-TAC-TOE")
print("player 1[X] --- player2[O]\n")
print()
print()
time.sleep(1)
while(Game == Running):
    os.system('cls')
    DrawBoard()
    if(player %2!=0):
        print("PLAYER 1 CHANCE")
        Mark = 'X'
    else:
        print("PLAYER 2 CHANCE")
        Mark = '0'
    choice=int(input("enter the position between [1-9] where you want to add the mark : "))
    try:
        if(CheckPosition(choice)):
           board[choice] = Mark
           player+=1
           CheckWin()
    except:
        print(" Its an invalid position!!! please enter position between[ 1 - 9 ]")
           

os.system('cls')
DrawBoard()
if(Game==Draw):
    print("GAME DRAW")
elif(Game==Win):
    player-=1
    if(player%2!=0):
        print("PLAYER 1 HAS WON")
    else:
        print("PLAYER 2 WON")

    
