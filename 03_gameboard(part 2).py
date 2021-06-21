"""
CS3B, Assignment #3, Tic Tac Toe, Part 2
Ulises Marian
"""

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
        if self is GameBoardPlayer.NONE:
            return " "
        else:
            return self.name


class ArrayGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        """
        Initialize a game board that internally represents the board using
        Python list of lists.
        :param nrows: number of rows
        :param ncols: number of columns
        """
        if nrows <= 0 or ncols <= 0:
            raise ValueError(f"Invalid nrows={nrows} ncols={ncols}")
        self.board = [[GameBoardPlayer.NONE for _ in range(ncols)]
                      for _ in range(nrows)]

    def get_nrows(self):
        return len(self.board)

    def get_ncols(self):
        return len(self.board[0])

    def set(self, row, col, value):
        """Set row/col on the board to value"""
        # No need to validate row/col ourselves; Python list[][] does that.
        self.board[row][col] = value

    def get(self, row, col):
        """Return the value at row/col on the board"""
        return self.board[row][col]

    # From here on, it's exactly the same code in both ArrayGameBoard and
    # BitGameBoard
    def __str__(self):
        s = ""
        for row in range(self.get_nrows()):
            # The row
            s += "|".join([str(self.get(row, col))
                           for col in range(self.get_ncols())]) + "\n"

            # The separator
            if row != self.get_nrows() - 1:
                s += "-+" * (self.get_ncols() - 1) + "-\n"
        return s

    def get_row_winner(self, row):
        """Given row index, see if there's a winner on that row"""

        # # Using Python's set and/or all() can make code shorter
        # if all(self.get(row, 0) == self.get(row, i) for i in range(self.get_ncols())):
        #     return self.get(row, 0)
        # else:
        #     return GameBoardPlayer.NONE

        # The code here shows how to do it with plain old for loop.
        for col in range(self.get_ncols()):
            if self.get(row, 0) != self.get(row, col):
                # If any other element on the row is different from the first
                # one, there's no winner in this row
                return GameBoardPlayer.NONE

        # Every element in the row is the same as the first, so it's a winner.
        # All elements may be NONE, but the caller checks for that.
        return self.get(row, 0)

    def get_col_winner(self, col):
        """Given column index, see if there's a winner on that column"""
        for row in range(self.get_nrows()):
            if self.get(0, col) != self.get(row, col):
                return GameBoardPlayer.NONE

        return self.get(0, col)

    def get_diag_winner(self):
        """If a square board, check if the two diagonals have winner"""
        if self.get_nrows() != self.get_ncols():
            return GameBoardPlayer.NONE

        # Get the winner in the \ diagonal
        upper_left = self.get(0, 0)
        if upper_left is not GameBoardPlayer.NONE:
            for row in range(self.get_nrows()):
                if upper_left != self.get(row, row):
                    break
            else:
                # If the for loop completes without break, all elements in
                # the diagonal is the same, so it's a winner
                return upper_left

        # Get the winner in the / diagonal
        upper_right = self.get(0, self.get_ncols() - 1)
        if upper_right is not GameBoardPlayer.NONE:
            col = self.get_ncols() - 1
            for row in range(self.get_nrows()):
                if upper_right != self.get(row, col):
                    break
                col -= 1
            else:
                return upper_right

        return GameBoardPlayer.NONE

    def check_for_draw(self):
        """Check if the game is DRAW; used after checking for winners."""
        for row in range(self.get_nrows()):
            for col in range(self.get_ncols()):
                if self.get(row, col) is GameBoardPlayer.NONE:
                    # If any space is unoccupied, it's not a draw
                    return GameBoardPlayer.NONE

        return GameBoardPlayer.DRAW


    def get_winner(self):
        """
        Get the winner on the board
        :return: one of GameBoardPlayer members to indicate the winner.
        """
        # Check for horizontal rows
        for row in range(self.get_nrows()):
            winner = self.get_row_winner(row)
            if winner is not GameBoardPlayer.NONE:
                return winner

        # Check for vertical columns
        for col in range(self.get_ncols()):
            winner = self.get_col_winner(col)
            if winner is not GameBoardPlayer.NONE:
                return winner

        # Check for diagonal if it's a square
        winner = self.get_diag_winner()
        if winner is not GameBoardPlayer.NONE:
            return winner

        # Finally, check for ties
        return self.check_for_draw()

    def get_winner_pythonic(self):
        # This is a succinct and pythonic way of writing get_winner().  It's not required
        # understanding, because it uses things we haven't covered, like nested function,
        # set(), and generator.
        # (Inspired by Shoshi C's solution.)

        def same(list_):
            """This returns True if all elements in list_ are the same, False otherwise"""

            # Convert list into set, and because set doesn't allow duplicate,
            # length of 1 means all elements in the list are the same element.
            return len(set(list_)) == 1

        def rows():
            # The commented line accesses the 2d list directly; actual line uses get()
            # yield from (row for row in self.board)
            yield from ([self.get(r, c) for c in range(self.get_ncols())] for r in range(self.get_nrows()))

        def cols():
            # zip(*self.board) transposes the board
            # yield from (row for row in zip(*self.board))
            yield from ([self.get(r, c) for r in range(self.get_nrows())] for c in range(self.get_ncols()))

        def combos():
            """This generates all rows, columns, then diagonals"""

            # We can return a complete list of all rows, columns and diagonals, but that's
            # likely wasteful if there's a winner on the board.  So use a generator instead
            # (that's the "yield" and "yield from"), so we only generate the next one if we
            # haven't found a winner yet.

            # Yield all rows
            yield from rows()

            # Yield all columns
            yield from cols()

            if self.get_nrows() == self.get_ncols():
                # Yield / diagonal
                # yield [row[i] for i, row in enumerate(self.board)]
                yield [self.get(i, i) for i in range(self.get_nrows())]
                # Yield | diagonal (reverse every row first, so \ becomes /)
                # yield [row[i] for i, row in enumerate(list(reversed(row)) for row in self.board)]
                yield [self.get(i, -i-1) for i in range(self.get_nrows())]

        # Check for winners in rows, columns, diagonals
        for combo in combos():
            if combo[0] is not GameBoardPlayer.NONE and same(combo):
                return combo[0]

        # If no winner, check if there's any empty space
        if any(GameBoardPlayer.NONE in row for row in rows()):
            return GameBoardPlayer.NONE

        # No winner and no empty space, it's a draw
        return GameBoardPlayer.DRAW


class BitGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.board = 0

    def get_nrows(self):
        return self.nrows

    def get_ncols(self):
        return self.ncols

    def set(self, row, col, player):
        mask = 0b11 << ((row * self.ncols + col) * 2)
        self.board &= ~mask
        self.board |= (player.value << ((row * self.ncols + col) * 2))

    def get(self, row, col):
        mask = 0b11 << ((row * self.ncols + col) * 2)
        mask &= self.board
        mask = mask >> ((row * self.ncols + col) * 2)
        if mask == 0b01:
            return GameBoardPlayer.X
        elif mask == 0b10:
            return GameBoardPlayer.O
        elif mask == 0b00:
            return GameBoardPlayer.NONE


    def __str__(self):
        s = ""
        for row in range(self.get_nrows()):
            # The row
            s += "|".join([str(self.get(row, col))
                           for col in range(self.get_ncols())]) + "\n"

            # The separator
            if row != self.get_nrows() - 1:
                s += "-+" * (self.get_ncols() - 1) + "-\n"
        return s

    def get_row_winner(self, row):
        """Given row index, see if there's a winner on that row"""

        # # Using Python's set and/or all() can make code shorter
        # if all(self.get(row, 0) == self.get(row, i) for i in range(self.get_ncols())):
        #     return self.get(row, 0)
        # else:
        #     return GameBoardPlayer.NONE

        # The code here shows how to do it with plain old for loop.
        for col in range(self.get_ncols()):
            if self.get(row, 0) != self.get(row, col):
                # If any other element on the row is different from the first
                # one, there's no winner in this row
                return GameBoardPlayer.NONE

        # Every element in the row is the same as the first, so it's a winner.
        # All elements may be NONE, but the caller checks for that.
        return self.get(row, 0)

    def get_col_winner(self, col):
        """Given column index, see if there's a winner on that column"""
        for row in range(self.get_nrows()):
            if self.get(0, col) != self.get(row, col):
                return GameBoardPlayer.NONE

        return self.get(0, col)

    def get_diag_winner(self):
        """If a square board, check if the two diagonals have winner"""
        if self.get_nrows() != self.get_ncols():
            return GameBoardPlayer.NONE

        # Get the winner in the \ diagonal
        upper_left = self.get(0, 0)
        if upper_left is not GameBoardPlayer.NONE:
            for row in range(self.get_nrows()):
                if upper_left != self.get(row, row):
                    break
            else:
                # If the for loop completes without break, all elements in
                # the diagonal is the same, so it's a winner
                return upper_left

        # Get the winner in the / diagonal
        upper_right = self.get(0, self.get_ncols() - 1)
        if upper_right is not GameBoardPlayer.NONE:
            col = self.get_ncols() - 1
            for row in range(self.get_nrows()):
                if upper_right != self.get(row, col):
                    break
                col -= 1
            else:
                return upper_right

        return GameBoardPlayer.NONE

    def check_for_draw(self):
        """Check if the game is DRAW; used after checking for winners."""
        for row in range(self.get_nrows()):
            for col in range(self.get_ncols()):
                if self.get(row, col) is GameBoardPlayer.NONE:
                    # If any space is unoccupied, it's not a draw
                    return GameBoardPlayer.NONE

        return GameBoardPlayer.DRAW

    def get_winner(self):
        """
        Get the winner on the board
        :return: one of GameBoardPlayer members to indicate the winner.
        """
        # Check for horizontal rows
        for row in range(self.get_nrows()):
            winner = self.get_row_winner(row)
            if winner is not GameBoardPlayer.NONE:
                return winner

        # Check for vertical columns
        for col in range(self.get_ncols()):
            winner = self.get_col_winner(col)
            if winner is not GameBoardPlayer.NONE:
                return winner

        # Check for diagonal if it's a square
        winner = self.get_diag_winner()
        if winner is not GameBoardPlayer.NONE:
            return winner

        # Finally, check for ties
        return self.check_for_draw()


class TicTacToeBoard:
    """A class that represents a Tic Tac Toe game board"""
    NROWS = 3
    NCOLS = 3

    def __init__(self):
        # The two game boards can be used interchangeably.
        self.board = ArrayGameBoard(self.NROWS, self.NCOLS)
        #self.board = BitGameBoard(self.NROWS, self.NCOLS)

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


class HumanPlayer:
    def __init__(self, side):
        self.side = side

    def __str__(self):
       s = f"The Human player is {self.side}"
       return s

    def get_move(self):
        valid = False   # loop until user types in valid row and column
        while not valid:
            user_move = input(f"Please input move for Human player"
                              f" {self.side} (row column): ")
            number_of_letters = len(user_move) - user_move.count(" ")
            if number_of_letters != 2:
                print("Invalid input. Exactly 2 numbers should be given.")
                continue

            row, col = user_move.split()
            try:
                row = int(row)
                col = int(col)
            except ValueError:
                print (f"Invalid input {user_move} : invalid literal "
                        f"for int() with base 10")
                continue

            valid = True

        print (f"Human player {self.side} makes move ({user_move})")
        my_tuple = tuple(map(int, user_move.split()))
        #returns a tuple of (row, column), both of which must be int.
        return my_tuple


def ttt_game(player1, player2):
    game = TicTacToeBoard()
    while game:
        mark = player1.get_move()
        # mark the row and col on the board as X or O
        # depending on the current player
        game.set(mark[0], mark[1], player1.side)
        print(game.__str__())        # display updated gameboard
        is_winner = game.get_winner()
        if is_winner == GameBoardPlayer.NONE:
            mark = player2.get_move()   # switch player to the opponent
            game.set(mark[0], mark[1], player2.side)  # and continue the loop
            print(game.__str__())
            is_winner = game.get_winner()
        if is_winner != GameBoardPlayer.NONE:
            print(f"Human Player {is_winner} wins")
            game = False

    return is_winner


#This is how to call ttt_game(), with 2 human players, one X and the other O
if __name__ == '__main__':
    ttt_game(player1 = HumanPlayer(GameBoardPlayer.X),
             player2 = HumanPlayer(GameBoardPlayer.O))


# testing BitGameBoard
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

    print()
    print(f"winner of board with 1 row of X is '{gb.get_winner()}':")

    # TODO add other tests (GameBoardPlayer.O, different rows, columns, diagonal, etc)
    print()
    print(gb)  # XXX in a row

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
    print(
        f"winner of board with diagonal (left to right) of X is '{gb.get_winner()}'")
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

    print(
        f"winner of board with diagonal (right to left) of O is '{gb.get_winner()}'")
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

    print(f"NO winner: '{gb.get_winner()}'")
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

    print(f"NO winner: '{gb.get_winner()}'")
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

    print(f"NO winner: '{gb.get_winner()}'")
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

    print(f"winner of board with ONE UNOCCUPIED space is: '{gb.get_winner()}'")
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

    print(f"winner of board with FOUR UNOCCUPIED spaces is: '{gb.get_winner()}'")
    print()

    # NONE
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

    print(
        f"winner of board with LOTS OF UNOCCUPIED spaces is: '{gb.get_winner()}'")
    print()

    # test get_nrows()
    print(f"The number of rows is: {gb.get_nrows()}")

    # test get_ncols()
    print(f"The number of columns is: {gb.get_ncols()}")


#if __name__ == '__main__':
    #The same tests should work for both types of *GameBoard
    #test_game_board(ArrayGameBoard(3, 3))
    #test_game_board(BitGameBoard(3, 3))
