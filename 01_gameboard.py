"""
CS3B, Assignment #1, Tic Tac Toe
Ulises Marian
"""

import time
from enum import Enum


class GameBoardPlayer(Enum):
    """
    An enum that represents a player on a game board; it's used to denote:
    . which player occupies a space on the board (can be NONE if unoccupied)
    . which player is the winner of the game (can be DRAW)
    """
    NONE = 0
    X = 1
    O = 2
    DRAW = 3


    def __str__(self):
        if self == self.NONE:    #alternative: if self is GameBoardPlayer.NONE:
            return " "
        else:
            return self.name

    
class ArrayGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        if nrows <= 0 or ncols <= 0:
            raise ValueError(f"{nrows} and {ncols} should be positive integers")
        self.nrows = nrows
        self.ncols = ncols
        self.gameboard = [[GameBoardPlayer.NONE] * ncols for _ in range(nrows)]
       

    def get_nrows(self):
        return self.nrows

    def get_ncols(self):
        return self.ncols

    def set(self, row, col, value):
        self.gameboard[row][col] = value

    def get(self, row, col):
        return self.gameboard[row][col]

    def __str__(self):
        s = ""
        for row in self.gameboard:
            for column in row:
                s += (f"{column}") + "|"
            s = s[:-1]
            s += "\n"    
            
            for column in row:
                s += "-+"
            s = s[:-1]

            s += "\n"
        s = s[:-7]
        return s
            

    def get_winner(self):
        for row in range(self.get_nrows()):
            for col in range(self.get_ncols()): 
                if self.get(0, 0) == GameBoardPlayer.X and self.get(0, 1) == GameBoardPlayer.X \
                   and self.get(0, 2) == GameBoardPlayer.X \
                   or self.get(1, 0) == GameBoardPlayer.X and self.get(1, 1) == GameBoardPlayer.X \
                   and self.get(1, 2) == GameBoardPlayer.X\
                   or self.get(2, 0) == GameBoardPlayer.X and self.get(2, 1) == GameBoardPlayer.X \
                   and self.get(2, 2) == GameBoardPlayer.X\
                   or self.get(0, 0) == GameBoardPlayer.X and self.get(1, 0) == GameBoardPlayer.X \
                   and self.get(2, 0) == GameBoardPlayer.X\
                   or self.get(0, 1) == GameBoardPlayer.X and self.get(1, 1) == GameBoardPlayer.X \
                   and self.get(2, 1) == GameBoardPlayer.X\
                   or self.get(0, 2) == GameBoardPlayer.X and self.get(1, 2) == GameBoardPlayer.X \
                   and self.get(2, 2) == GameBoardPlayer.X\
                   or self.get(0, 0) == GameBoardPlayer.X and self.get(1, 1) == GameBoardPlayer.X \
                   and self.get(2, 2) == GameBoardPlayer.X\
                   or self.get(0, 2) == GameBoardPlayer.X and self.get(1, 1) == GameBoardPlayer.X \
                   and self.get(2, 0) == GameBoardPlayer.X:
                    return "X"
                elif self.get(0, 0) == GameBoardPlayer.O and self.get(0, 1) == GameBoardPlayer.O \
                   and self.get(0, 2) == GameBoardPlayer.O \
                   or self.get(1, 0) == GameBoardPlayer.O and self.get(1, 1) == GameBoardPlayer.X \
                   and self.get(1, 2) == GameBoardPlayer.O\
                   or self.get(2, 0) == GameBoardPlayer.O and self.get(2, 1) == GameBoardPlayer.O \
                   and self.get(2, 2) == GameBoardPlayer.O\
                   or self.get(0, 0) == GameBoardPlayer.O and self.get(1, 0) == GameBoardPlayer.O \
                   and self.get(2, 0) == GameBoardPlayer.O\
                   or self.get(0, 1) == GameBoardPlayer.O and self.get(1, 1) == GameBoardPlayer.O \
                   and self.get(2, 1) == GameBoardPlayer.O\
                   or self.get(0, 2) == GameBoardPlayer.O and self.get(1, 2) == GameBoardPlayer.O \
                   and self.get(2, 2) == GameBoardPlayer.O\
                   or self.get(0, 0) == GameBoardPlayer.O and self.get(1, 1) == GameBoardPlayer.O \
                   and self.get(2, 2) == GameBoardPlayer.O\
                   or self.get(0, 2) == GameBoardPlayer.O and self.get(1, 1) == GameBoardPlayer.O \
                   and self.get(2, 0) == GameBoardPlayer.O: 
                    return "O"
                elif self.get(0, 0) == GameBoardPlayer.NONE or self.get(0, 1) == GameBoardPlayer.NONE \
                   or self.get(0, 2) == GameBoardPlayer.NONE \
                   or self.get(1, 0) == GameBoardPlayer.NONE or self.get(1, 1) == GameBoardPlayer.NONE \
                   or self.get(1, 2) == GameBoardPlayer.NONE\
                   or self.get(2, 0) == GameBoardPlayer.NONE or self.get(2, 1) == GameBoardPlayer.NONE \
                   or self.get(2, 2) == GameBoardPlayer.NONE\
                   or self.get(0, 0) == GameBoardPlayer.NONE or self.get(1, 0) == GameBoardPlayer.NONE \
                   or self.get(2, 0) == GameBoardPlayer.NONE\
                   or self.get(0, 1) == GameBoardPlayer.NONE or self.get(1, 1) == GameBoardPlayer.NONE \
                   or self.get(2, 1) == GameBoardPlayer.NONE\
                   or self.get(0, 2) == GameBoardPlayer.NONE or self.get(1, 2) == GameBoardPlayer.NONE \
                   or self.get(2, 2) == GameBoardPlayer.NONE\
                   or self.get(0, 0) == GameBoardPlayer.NONE or self.get(1, 1) == GameBoardPlayer.NONE \
                   or self.get(2, 2) == GameBoardPlayer.NONE\
                   or self.get(0, 2) == GameBoardPlayer.NONE or self.get(1, 1) == GameBoardPlayer.NONE \
                   or self.get(2, 0) == GameBoardPlayer.NONE:
                    return "NONE"
                else:
                    return "DRAW"
              

class BitGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        pass

    def get_nrows(self):
        pass

    def get_ncols(self):
        pass

    def set(self, row, col, player):
        pass

    def get(self, row, col):
        pass

    def __str__(self):
        return "(To be implemented)"

    def get_winner(self):
        return GameBoardPlayer.NONE


class TicTacToeBoard:
    """
    A class that represents a Tic Tac Toe game board.
    It's a thin wrapper around the actual game board
    """
    NROWS = 3
    NCOLS = 3

    def __init__(self):
        # The two game boards can be used interchangeably.
        self.board = ArrayGameBoard(self.NROWS, self.NCOLS)
        # self.board = BitGameBoard(self.NROWS, self.NCOLS)

    def set(self, row, col, value):
        if self.board.get(row, col) != GameBoardPlayer.NONE:
            raise ValueError(f"{row} {col} already has {self.board.get(row, col)}")
        self.board.set(row, col, value)

    def clear(self, row, col):
        self.board.set(row, col, GameBoardPlayer.NONE)

    def get(self, row, col):
        return self.board.get(row, col)

    def get_winner(self):
        return self.board.get_winner()

    def __str__(self):
        return self.board.__str__()


def test_game_board(gb):
    # Test __str__()
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.X)
    gb.set(0, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))

    try:
        gb.get(100, 100)
        print("gb.get(100, 100) fails to raise IndexError")
    except IndexError:
        print("gb.get(100, 100) correctly raises IndexError")

    print()
    print(f"winner of board with 1 row of X is '{gb.get_winner()}':")

    # TODO add other tests (GameBoardPlayer.O, different rows, columns, diagonal, etc)
    print()
    print(gb)   # XXX in a row

    print()
    # set O in second column
    gb.set(0, 1, GameBoardPlayer.O)
    gb.set(1, 1, GameBoardPlayer.O)
    gb.set(2, 1, GameBoardPlayer.O)
    print("gb.get(0, 0) returns", gb.get(0, 1))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(2, 1))
    print()
    print(gb)
    print(f"winner of board with 2nd column of O is '{gb.get_winner()}'")
    print()

    # set X in diagonal
    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(1, 1, GameBoardPlayer.X)
    gb.set(2, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)
    print(f"winner of board with diagonal (left to right) of X is '{gb.get_winner()}'")
    print()

    # set O in diagonal (right to left)
    gb.set(0, 2, GameBoardPlayer.O)
    gb.set(1, 1, GameBoardPlayer.O)
    gb.set(2, 0, GameBoardPlayer.O)
    print("gb.get(0, 0) returns", gb.get(0, 2))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(2, 0))
    print()
    print(gb)

    print(f"winner of board with diagonal (right to left) of O is '{gb.get_winner()}'")
    print()

    # set X in third row
    gb.set(2, 0, GameBoardPlayer.X)
    gb.set(2, 1, GameBoardPlayer.X)
    gb.set(2, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(2, 0))
    print("gb.get(0, 1) returns", gb.get(2, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)

    print(f"winner of board with 3rd row of X is '{gb.get_winner()}'")

    print()
    # draw
    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.O)
    gb.set(0, 2, GameBoardPlayer.X)
    gb.set(1, 0, GameBoardPlayer.O)
    gb.set(1, 1, GameBoardPlayer.X)
    gb.set(1, 2, GameBoardPlayer.X)
    gb.set(2, 0, GameBoardPlayer.O)
    gb.set(2, 1, GameBoardPlayer.X)
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(1, 2))
    print("gb.get(0, 0) returns", gb.get(2, 0))
    print("gb.get(0, 1) returns", gb.get(2, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)

    print(f"NO winner: {gb.get_winner()}")
    print()
    
    # another draw
    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.O)
    gb.set(0, 2, GameBoardPlayer.O)
    gb.set(1, 0, GameBoardPlayer.O)
    gb.set(1, 1, GameBoardPlayer.X)
    gb.set(1, 2, GameBoardPlayer.X)
    gb.set(2, 0, GameBoardPlayer.X)
    gb.set(2, 1, GameBoardPlayer.O)
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(1, 2))
    print("gb.get(0, 0) returns", gb.get(2, 0))
    print("gb.get(0, 1) returns", gb.get(2, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)

    print(f"NO winner: {gb.get_winner()}")
    print()
    
    # yet another draw
    gb.set(0, 0, GameBoardPlayer.O)
    gb.set(0, 1, GameBoardPlayer.X)
    gb.set(0, 2, GameBoardPlayer.X)
    gb.set(1, 0, GameBoardPlayer.X)
    gb.set(1, 1, GameBoardPlayer.O)
    gb.set(1, 2, GameBoardPlayer.O)
    gb.set(2, 0, GameBoardPlayer.O)
    gb.set(2, 1, GameBoardPlayer.X)
    gb.set(2, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(1, 2))
    print("gb.get(0, 0) returns", gb.get(2, 0))
    print("gb.get(0, 1) returns", gb.get(2, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)

    print(f"NO winner: {gb.get_winner()}")
    print()
    
    # NONE - no winner yet
    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.X)
    gb.set(0, 2, GameBoardPlayer.O)
    gb.set(1, 0, GameBoardPlayer.X)
    gb.set(1, 1, GameBoardPlayer.NONE)
    gb.set(1, 2, GameBoardPlayer.O)
    gb.set(2, 0, GameBoardPlayer.O)
    gb.set(2, 1, GameBoardPlayer.X)
    gb.set(2, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(1, 2))
    print("gb.get(0, 0) returns", gb.get(2, 0))
    print("gb.get(0, 1) returns", gb.get(2, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)

    print(f"winner of board with ONE UNOCCUPIED space is: {gb.get_winner()}")
    print()
    
    # NONE
    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.NONE)
    gb.set(0, 2, GameBoardPlayer.O)
    gb.set(1, 0, GameBoardPlayer.X)
    gb.set(1, 1, GameBoardPlayer.NONE)
    gb.set(1, 2, GameBoardPlayer.NONE)
    gb.set(2, 0, GameBoardPlayer.O)
    gb.set(2, 1, GameBoardPlayer.NONE)
    gb.set(2, 2, GameBoardPlayer.X)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(1, 2))
    print("gb.get(0, 0) returns", gb.get(2, 0))
    print("gb.get(0, 1) returns", gb.get(2, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)

    print(f"winner of board with FOUR UNOCCUPIED spaces is: {gb.get_winner()}")
    print()

    #NONE
    gb.set(0, 0, GameBoardPlayer.O)
    gb.set(0, 1, GameBoardPlayer.NONE)
    gb.set(0, 2, GameBoardPlayer.O)
    gb.set(1, 0, GameBoardPlayer.NONE)
    gb.set(1, 1, GameBoardPlayer.NONE)
    gb.set(1, 2, GameBoardPlayer.NONE)
    gb.set(2, 0, GameBoardPlayer.O)
    gb.set(2, 1, GameBoardPlayer.NONE)
    gb.set(2, 2, GameBoardPlayer.O)
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))
    print("gb.get(0, 0) returns", gb.get(1, 0))
    print("gb.get(0, 1) returns", gb.get(1, 1))
    print("gb.get(0, 2) returns", gb.get(1, 2))
    print("gb.get(0, 0) returns", gb.get(2, 0))
    print("gb.get(0, 1) returns", gb.get(2, 1))
    print("gb.get(0, 2) returns", gb.get(2, 2))
    print()
    print(gb)

    print(f"winner of board with LOTS OF UNOCCUPIED spaces is: {gb.get_winner()}")
    print()

    # raise IndexError
    gb.set(0, 0, GameBoardPlayer.O)
    gb.set(0, 1, GameBoardPlayer.NONE)
    gb.set(0, 2, GameBoardPlayer.O)
    gb.set(1, 0, GameBoardPlayer.NONE)
    gb.set(1, 1, GameBoardPlayer.NONE)
    gb.set(1, 2, GameBoardPlayer.NONE)

    try:
        gb.get(6, 4)
        print("gb.get(6, 4) fails to raise IndexError")
    except IndexError:
        print("gb.get(6, 4) correctly raises IndexError")

    # fails to raise IndexError
    try:
        gb.get(2, 2)
        print("gb.get(2, 2) fails to raise IndexError")
    except IndexError:
        print("gb.get(2, 2) correctly raises IndexError")

    # fails to raise IndexError
    try:
        gb.get(1, 1)
        print("gb.get(1, 1) fails to raise IndexError")
    except IndexError:
        print("gb.get(1, 1) correctly raises IndexError")

    # correctly raises IndexError
    try:
        gb.set(9, 1, GameBoardPlayer.O )
        print("gb.set(9, 1, GameBoardPlayer.O) fails to raise IndexError")
    except IndexError:
        print("gb.set(9, 1, GameBoardPlayer.O) correctly raises IndexError")

    # correctly raises IndexError
    try:
        gb.set(2, 7, GameBoardPlayer.NONE )
        print("gb.set(2, 7, GameBoardPlayer.NONE) fails to raise IndexError")
    except IndexError:
        print("gb.set(2, 7, GameBoardPlayer.NONE) correctly raises IndexError")

    print()
    
    # test get_nrows()
    print(f"The number of rows is: {gb.get_nrows()}")

    # test get_ncols()
    print(f"The number of columns is: {gb.get_ncols()}")
    

if __name__ == '__main__':
    # The same tests should work for both types of *GameBoard
    test_game_board(ArrayGameBoard(3, 3))
     #test_game_board(BitGameBoard(3, 3))
