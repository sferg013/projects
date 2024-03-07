import random
cnt=1
def TicTT(L,cnt):
    print("Round "+str(cnt))
    j=0
    for j in range(len(L)):
        print(L[j])
    print("player 1: ")
    a=int(input("Player 1 First coord"))
    b=int(input("Player 1 second coord"))

    L[a][b]=1
    if win(L):
        return
    #for k in range(len(L)):
     #   print(L[k])
    print("player 2: ")
    c=int(input("Player 2 first coord"))
    d=int(input("Player 2 second coord"))

    L[c][d]=2
    if win(L):
        return
        
    cnt=cnt+1
    TicTT(L,cnt)
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
