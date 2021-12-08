"""
Tic Tac Toe Player
"""

import copy
from os import X_OK


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if X or O in board:
        Countx = 0
        Counto = 0
        for x in board:
            for y in x:
                if y == X:
                    Countx+=1
                if y == O:
                    Counto+=1
        if Countx > Counto:
            return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    CountX=0
    CountY=0
    actions= set()
    for X in board:
        for Y in X:
            if Y == EMPTY:
                actions.add((CountX,CountY))
            CountY+=1
        CountX+=1
        CountY=0
    if len(actions) == 0: return EMPTY
    else: return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    acDimx= action[0]
    acDimy= action[1]
    boardcopy = copy.deepcopy(board)
    if(board[acDimx][acDimy]==EMPTY):
        boardcopy[acDimx][acDimy]= player(board)
    else:
        raise NameError("Wrong Move Lad")
    return boardcopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    Win = None
    vertical = [list(i) for i in zip(*board)]
    for X in board:
        if(X[0] == X[1] == X[2]):
            Win = X[1]
    for Y in vertical:
        if(Y[0] == Y[1] == Y[2]):
            Win = Y[1]
    if (board[0][0]== board[1][1]==board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        if(board[1][1] != EMPTY):
            Win = board[1][1]
    return Win



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for X in board:
            if EMPTY in X:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    return None  


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    OpMove= set()
    for action in actions(board):
        if player(board) == X:
            if(MaxValue(result(board,action)) >= 0):
                OpMove.add(action)
        if player(board) == O:
            if(MinValue(result(board,action)) <= 0):
                OpMove.add(action)
    return OpMove.pop() 

def MinValue(board):
    v = -10
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,MaxValue(result(board,action)))
    return v

def MaxValue(board):
    v = 10
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v,MinValue(result(board,action)))
    return v