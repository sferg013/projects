import random
cnt=1
def TicTT(L,cnt):
    print("Round "+str(cnt))
    j=0
    for j in range(len(L)):
        print(L[j])
    print("player 1: ")
    a,b=coords(L,1)

    L[a][b]=1
    if win(L):
        return
    #for k in range(len(L)):
     #   print(L[k])
    print("player 2: ")
    c,d=coords(L,2)

    L[c][d]=2
    if win(L):
        return
        
    cnt=cnt+1
    TicTT(L,cnt)
def coords(L,n):
    x=int(input("Player "+str(n) +" First coord"))
    y=int(input("Player "+str(n) +" second coord"))
    if L[x][y]==0:
        return(x,y)
    else:
        print("try again")
    return coords(L,n)


    #for m in range(len(L)):
     #   print(L[m])
    #winning cases: exact points = true but want more effecent less lines of code
def win(L):
    for i in range(3):
        if L[i][0]==1 and L[i][1]==1 and L[i][2]==1:
            print("player 1 wins")
            for j in range(len(L)):
                print(L[j])
            return(True)
        elif L[i][0]==2 and L[i][1]==2 and L[i][2]==2:
            print("player 2 wins")
            for j in range(len(L)):
                print(L[j])
            return True
        elif L[0][i]==1 and L[1][i]==1 and L[2][i]==1:
            print("player 1 wins")
            for j in range(len(L)):
                print(L[j])
            return True
        elif L[0][i]==2 and L[1][i]==2 and L[2][i]==2:
            print("player 2 wins")
            for j in range(len(L)):
                print(L[j])
            return True
        elif L[0][0]==1 and L[1][1]==1 and L[2][2]==1:
            print("player 1 wins")
            for j in range(len(L)):
                print(L[j])
            return True
        elif L[0][0]==2 and L[1][1]==2 and L[2][2]==2:
            print("player 2 wins")
            for j in range(len(L)):
                print(L[j])
            return True
        elif L[0][2]==1 and L[1][1]==1 and L[2][0]==1:
            print("player 1 wins")
            for j in range(len(L)):
                print(L[j])
            return True
        elif L[0][2]==2 and L[1][1]==2 and L[2][0]==2:
            print("player 2 wins")
            for j in range(len(L)):
                print(L[j])
            return True



print("welcome to tic tac toe")
L =[[0,0,0],[0,0,0],[0,0,0]]
TicTT(L,cnt)
