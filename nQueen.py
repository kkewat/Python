from math import *
import sys
x = {}
n = int(input("enter the no. of queens : "))

def myfunction():
    myfunction.counter += 1
    return(myfunction.counter)
myfunction.counter = 0
    
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
                    print(x[j],end=" ")
                print()
                print('........')
                myfunction()
            else:
                nQueens(k+1)
            
nQueens(1)
print("The total number of possible solutions :",myfunction()-1)

            
