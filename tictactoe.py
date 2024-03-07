import random
def TicTT(L):
    print("welcome to tic tac toe")
    
    for j in range(len(L)):
        print(L[j])
    print("player 1: ")
    a=int(input())
    b=int(input())

    L[a][b]=1
    for k in range(len(L)):
        print(L[k])
    print("player 2: ")
    c=int(input())
    d=int(input())

    L[c][d]=2
    for i in range(len(L)):
        print(L[i])
    i=0
    #winning cases: exact points = true but want more effecent less lines of code
    for i in range(3):
        if L[i][0]==1 and L[i][1]==1 and L[i][2]==1:
            print("player 1 wins")
            return None
        elif L[i][0]==2 and L[i][1]==2 and L[i][2]==2:
            print("player 2 wins")
            return None
        elif L[0][i]==1 and L[1][i]==1 and L[2][i]==1:
            print("player 1 wins")
            return None
        elif L[0][i]==2 and L[1][i]==2 and L[2][i]==2:
            print("player 2 wins")
            return None
        else:
            TicTT(L)



L =[[0,0,0],[0,0,0],[0,0,0]]
TicTT(L)
