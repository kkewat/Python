from math import *
import sys
x = {}
n = int(input("enter the no. of queens : "))

def Count():
    Count.counter += 1
    return(Count.counter)
Count.counter = 0

def Drawboard(position):
    board=[]
    for column in range(n):
        if(column == position-1):
            board.append(1)
        else:
            board.append(0)

    print(*board,sep="  ")
  
def clear_future_blocks(k):
    for i in range(k,n+1):
        x[i] = None

def Place(k,i):
    if(i in x.values()):
        return False
    j = 1
    while(j<k):
        if abs(x[j]-i) == abs(j-k):
            return False
        j += 1
    return True

def nQueens(k):
    for i in range(1,n+1):
        clear_future_blocks(k)
        if Place(k,i):
            x[k] = i
            if(k==n):
                for j in x:
                    Drawboard(x[j])
                print()
                print('.'*20)
                Count()
            else:
                nQueens(k+1)
            
nQueens(1)
print("The total number of possible solutions :",Count()-1)

            
