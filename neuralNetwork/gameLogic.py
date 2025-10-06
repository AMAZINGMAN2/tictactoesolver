import numpy



class Board:
    def __init__(self):
        self.board = numpy.array([[-1,-1,-1],
                                 [-1,-1,-1], 
                                 [-1,-1,-1]])

    def clear(self):
        self.board.fill(-1)
    def set(self, coordinate, value):
        self.board[coordinate[0], coordinate[1]] = value
    def getValidMove(self):
        row, col = numpy.where(self.board == -1)
        return list(zip(row,col))
        


def win(boar):
    bory = boar
    boar = boar.board
    if (boar[0][0] == 0 and boar[0][1] == 0 and boar[0][2] == 0) or (boar[1][0] == 0 and boar[1][1] == 0 and boar[1][2] == 0) or (boar[2][0] == 0 and boar[2][1] == 0 and boar[2][2] == 0) or (boar[0][0] == 0 and boar[1][0] == 0 and boar[2][0] == 0) or (boar[0][1] == 0 and boar[1][1] == 0 and boar[2][1] == 0) or (boar[0][2] == 0 and boar[1][2] == 0 and boar[2][2] == 0) or (boar[0][0] == 0 and boar[1][1] == 0 and boar[2][2] == 0) or (boar[0][2] == 0 and boar[1][1] == 0 and boar[2][0] == 0):
        return 0
    if (boar[0][0] == 1 and boar[0][1] == 1 and boar[0][2] == 1) or (boar[1][0] == 1 and boar[1][1] == 1 and boar[1][2] == 1) or (boar[2][0] == 1 and boar[2][1] == 1 and boar[2][2] == 1) or (boar[0][0] == 1 and boar[1][0] == 1 and boar[2][0] == 1) or (boar[0][1] == 1 and boar[1][1] == 1 and boar[2][1] == 1) or (boar[0][2] == 1 and boar[1][2] == 1 and boar[2][2] == 1) or (boar[0][0] == 1 and boar[1][1] == 1 and boar[2][2] == 1) or (boar[0][2] == 1 and boar[1][1] == 1 and boar[2][0] == 1):
        return 1
    if bory.getValidMove() == []:
        return -1
    return None

# O is 0 and X is 1
def encode(board):
    return board.flatten()

def reward(board, player):
    result = win(board)
    if result == -1: # tie
        return 0
    elif result == player:
        return 1
    else:
        return -1

def play():
    board = Board()
    win(board)
    # board.clear()
    board.set([1,2], 1)
    print(board.getValidMove())
    encodedBoard = encode(board.board)
    print(board.board)
    

play()
