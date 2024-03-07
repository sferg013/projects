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

    #winning cases: exact points = true but want more effecent less lines of code

def win(L):
    for p in [1, 2]:
        # Check rows and columns
        for i in range(3):
            if all(L[i][j] == p for j in range(3)) or all(L[j][i] == p for j in range(3)):
                print(f"Player {p} wins")
                for k in range(len(L)):
                    print(L[k])
                return True

        # Check diagonals
        if all(L[i][i] == p for i in range(3)) or all(L[i][2 - i] == p for i in range(3)):
            print(f"Player {p} wins")
            for k in range(len(L)):
                print(L[k])
            return True

    return False

print("welcome to tic tac toe")
L =[[0,0,0],[0,0,0],[0,0,0]]
TicTT(L,cnt)
