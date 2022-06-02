"""
Tic Tac Toe Player
"""

import math

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
    start = True
    countx = 0
    counto = 0
    for line in board:
        countx += line.count(X)
        counto += line.count(O)

    if (countx > counto):
        return O
    else:
        return X



def actions(board):
    possible = set()
    countline = 0
    for line in board:
        countvalue = 0
        for value in line:
            if value is EMPTY:
                possible.push(countline,countvalue)
            countvalue = countvalue + 1
        countline = countline + 1
    

    return possible


def result(board, action):
    
    mboard = deepcopy(board)
    
    turnplayer = player(board)
    
    i,j = action
    
    if (mboard[i][j] == None):
        raise Exception("Action error")
    else:
        mboard[i][j] = turnplayer
    
    return mboard


def winner(board):
    
    for player in (X,O):
        for line in board:
            if (line == [player * 3]):
                return player
    
        for i in range(3):
        column = [board[x][i] for x in range(3)]
        if (column == [player * 3]):
            return player

        for i in range(3):
            if (board[i][i]==[player *3]):
                return player
            elif(board[i][-i] == [player * 3]):
                return player
    return None

def terminal(board):
    
    if(winner(board) = True):
        return True
    elif(actions(board = False)):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
   result = winner(board)

   if(result == X):
       return 1
    elif(result == 0):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    v = -INFINITY
    if terminal(board):
        return utility(board)

    for action in actions(board):
        # get the resulting board for a given action
        resulting_board = result(board, action)
        # check the best option for the next player
        v = max(v, min(resulting_board))
    
    return v


def min_value(board):

    v = INFINITY
    if terminal(board):
        return utility(board)

    for action in actions(board):
        # get the resulting board for a given action
        resulting_board = result(board, action)
        # check the best option for the next player
        v = min(v, max(resulting_board))
    
    return v