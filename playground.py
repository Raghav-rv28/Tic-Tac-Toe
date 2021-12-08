

"""
X = "X"
O = "O"
EMPTY = None
board =      [[X, O, O],
              [O, EMPTY, X],
              [X, O, X]]



CountX = 0
CountY= 0
actions= set()
for X in board:
    for Y in X:
        if Y == EMPTY:
            actions.add((str(CountX+1),str(CountY+1)))
        CountY+=1
    CountX+=1
    CountY=0



Win = None
vertical = [list(i) for i in zip(*board)]
for X in board:
    if(X[0] == X[1] == X[2]):
        Win = X[1]
        print("Horizontal Win",Win)
for Y in vertical:
    if(Y[0] == Y[1] == Y[2]):
        Win = Y[1]
        print("Vertical Win",Win)
if (board[0][0]== board[1][1]==board[2][2] or board[0][2] == board[1][1] == board[2][0]):
    Win = board[1][1]
    print("Diagonal Win",Win)

for X in board:
    if EMPTY in X:
        print("yes i am here")"""