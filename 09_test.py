"""
CS3B, Assignment #9, AI Tic Tac Toe Player
Ulises Marian
testing
"""
import unittest

from assignment09 import *


class PlayerTestCase(unittest.TestCase):
    def testStr(self):
        self.assertEqual(" ", str(GameBoardPlayer.NONE))
        self.assertEqual("X", str(GameBoardPlayer.X))
        self.assertEqual("O", str(GameBoardPlayer.O))
        self.assertEqual("DRAW", str(GameBoardPlayer.DRAW))


class GameBoardTestCase(unittest.TestCase):
    GAME_BOARD_TYPE = None
    BOARD_DIMS = (
        (3, 3),
        (2, 5),
    )

    SQUARE_BOARD_DIMS = (
        (3, 3),
        (5, 5),
    )

    def testInitGetN(self):
        for nrows, ncols in self.BOARD_DIMS:
            with self.subTest(f"{nrows}, {ncols}"):
                board = self.GAME_BOARD_TYPE(nrows, ncols)
                self.assertEqual(nrows, board.get_nrows())
                self.assertEqual(ncols, board.get_ncols())

    def testInitGet(self):
        for nrows, ncols in self.BOARD_DIMS:
            with self.subTest(f"{nrows}, {ncols}"):
                board = self.GAME_BOARD_TYPE(nrows, ncols)
                for row in range(nrows):
                    for col in range(ncols):
                        self.assertIs(GameBoardPlayer.NONE, board.get(row, col))

    def testSetGet(self):
        boards = (
            (
                (0, 1, 2),
                (2, 1, 2),
                (2, 1, 0),
            ),
            (
                (0, 1, 0, 1, 0),
                (2, 1, 0, 1, 2),
            )
        )

        for b in boards:
            nrows, ncols = len(b), len(b[0])
            board = self.GAME_BOARD_TYPE(nrows, ncols)
            for row in range(nrows):
                for col in range(ncols):
                    board.set(row, col, GameBoardPlayer(b[row][col]))

            for row in range(nrows):
                for col in range(ncols):
                    with self.subTest(f"{nrows}, {ncols}, {row}, {col}"):
                        self.assertIs(b[row][col], board.get(row, col).value, f"\n{board}")

    def testGetInvalid(self):
        for nrows, ncols in self.BOARD_DIMS:
            bad_row_cols = (
                # (-1, 0),     # -1 is the last elements, so ok
                (-nrows - 1, 0),
                (nrows, 0),
                (0, -ncols - 1),
                (0, ncols),
                (-nrows - 1, -ncols - 1),
                (nrows, ncols),
            )
            for bad_row, bad_col in bad_row_cols:
                board = self.GAME_BOARD_TYPE(nrows, ncols)
                with self.subTest(f"get {nrows}, {ncols}, {bad_row}, {bad_col}"):
                    with self.assertRaises(IndexError):
                        board.get(bad_row, bad_col)

                with self.subTest(f"set {nrows}, {ncols}, {bad_row}, {bad_col}"):
                    with self.assertRaises(IndexError):
                        board.set(bad_row, bad_col, GameBoardPlayer.NONE)

    def testInitFailure(self):
        dims = {
            (0, 1),
            (1, 0),
        }
        for nrows, ncols in dims:
            with self.subTest(f"{nrows}, {ncols}"):
                with self.assertRaises(ValueError):
                    self.GAME_BOARD_TYPE(nrows, ncols)

    def testStr1(self):
        for nrows, ncols in self.BOARD_DIMS:
            with self.subTest(f"{nrows}, {ncols}"):
                board = self.GAME_BOARD_TYPE(nrows, ncols)
                board.set(1, 1, GameBoardPlayer.X)
                self.assertEqual(str, type(board.__str__()))
                print(board)

    def testStr2(self):
        # It's ok if some of these tests fail, if they are just some slight
        # differences in the str representation.
        dim_str = {
            (3, 3): " | | \n-+-+-\n |X| \n-+-+-\n | | \n",
            (2, 5): " | | | | \n-+-+-+-+-\n |X| | | \n"
        }
        for (nrows, ncols), s in dim_str.items():
            with self.subTest(f"{nrows}, {ncols}"):
                board = self.GAME_BOARD_TYPE(nrows, ncols)
                board.set(1, 1, GameBoardPlayer.X)
                self.assertEqual(s, board.__str__(), f"\nexpected=\n{s}\nactual=\n{board.__str__()}")

    def testGetWinnerAll(self):
        for nrows, ncols in self.BOARD_DIMS:
            for player in (GameBoardPlayer.X, GameBoardPlayer.O):
                with self.subTest(f"{nrows}, {ncols}, {player}"):
                    board = self.GAME_BOARD_TYPE(nrows, ncols)
                    # Set the whole board to be the same, in case some solutions
                    # just check if the board is full and simply returns NONE
                    # instead of checking for a winner first
                    for row in range(nrows):
                        for col in range(ncols):
                            board.set(row, col, player)
                    self.assertEqual(player, board.get_winner(), f"\n{board}")

    def testGetWinnerRow(self):
        for nrows, ncols in self.BOARD_DIMS:
            for player in (GameBoardPlayer.X, GameBoardPlayer.O):
                for row in range(nrows):
                    with self.subTest(f"{nrows}, {ncols}, {player}, {row}"):
                        board = self.GAME_BOARD_TYPE(nrows, ncols)
                        for col in range(ncols):
                            board.set(row, col, player)
                        self.assertEqual(player, board.get_winner(), f"\n{board}")

    def testGetWinnerRowOddBallCase(self):
        # Some students remember the last set mark (X or O) and compare all
        # the rows/column against that, hence this special test.
        nrows, ncols = 3, 3
        player = GameBoardPlayer.X
        row = 1
        with self.subTest(f"{nrows}, {ncols}, {player}, {row}"):
            board = self.GAME_BOARD_TYPE(nrows, ncols)
            for col in range(ncols):
                board.set(row, col, player)
            board.set(row + 1, col, GameBoardPlayer.O)
            self.assertEqual(player, board.get_winner(), f"\n{board}")

    def testGetWinnerColumn(self):
        for nrows, ncols in self.BOARD_DIMS:
            for player in (GameBoardPlayer.X, GameBoardPlayer.O):
                for col in range(ncols):
                    with self.subTest(f"{nrows}, {ncols}, {player}, {col}"):
                        board = self.GAME_BOARD_TYPE(nrows, ncols)
                        for row in range(nrows):
                            board.set(row, col, player)
                        self.assertEqual(player, board.get_winner(), f"\n{board}")

    def testGetWinnerDiagBackSlash(self):
        # diagonal \
        for nrows, ncols in self.SQUARE_BOARD_DIMS:
            for player in (GameBoardPlayer.X, GameBoardPlayer.O):
                with self.subTest(f"{nrows}, {ncols}, {player}"):
                    board = self.GAME_BOARD_TYPE(nrows, ncols)
                    for row in range(nrows):
                        board.set(row, row, player)
                    self.assertEqual(player, board.get_winner(), f"\n{board}")

    def testGetWinnerDiagForwardSlash(self):
        # diagonal /
        for nrows, ncols in self.SQUARE_BOARD_DIMS:
            for player in (GameBoardPlayer.X, GameBoardPlayer.O):
                with self.subTest(f"{nrows}, {ncols}, {player}"):
                    board = self.GAME_BOARD_TYPE(nrows, ncols)
                    col = ncols - 1
                    for row, col in zip(range(nrows), range(ncols - 1, -1, -1)):
                        board.set(row, col, player)
                    self.assertEqual(player, board.get_winner(), f"\n{board}")

    def testGetWinnerDiagNoneSquare(self):
        board = self.GAME_BOARD_TYPE(2, 5)
        board.set(0, 0, GameBoardPlayer.O)
        board.set(1, 1, GameBoardPlayer.O)
        self.assertIs(GameBoardPlayer.NONE, board.get_winner())

    def testGetWinnerDraw1(self):
        nrows, ncols = 3, 4
        board = self.GAME_BOARD_TYPE(nrows, ncols)
        board.set(0, 0, GameBoardPlayer.X)
        board.set(0, 1, GameBoardPlayer.O)
        board.set(0, 2, GameBoardPlayer.X)
        board.set(0, 3, GameBoardPlayer.O)

        board.set(1, 0, GameBoardPlayer.X)
        board.set(1, 1, GameBoardPlayer.O)
        board.set(1, 2, GameBoardPlayer.X)
        board.set(1, 3, GameBoardPlayer.O)

        board.set(2, 0, GameBoardPlayer.O)
        board.set(2, 1, GameBoardPlayer.X)
        board.set(2, 2, GameBoardPlayer.O)
        board.set(2, 3, GameBoardPlayer.X)

        self.assertEqual(GameBoardPlayer.DRAW, board.get_winner())

    def helpMakeBoardWithDraw(self):
        nrows, ncols = 3, 3
        board = self.GAME_BOARD_TYPE(nrows, ncols)
        board.set(0, 0, GameBoardPlayer.X)
        board.set(0, 1, GameBoardPlayer.O)
        board.set(0, 2, GameBoardPlayer.X)

        board.set(1, 0, GameBoardPlayer.X)
        board.set(1, 1, GameBoardPlayer.O)
        board.set(1, 2, GameBoardPlayer.X)

        board.set(2, 0, GameBoardPlayer.O)
        board.set(2, 1, GameBoardPlayer.X)
        board.set(2, 2, GameBoardPlayer.O)
        return board

    def testGetWinnerDraw2(self):
        board = self.helpMakeBoardWithDraw()
        self.assertEqual(GameBoardPlayer.DRAW, board.get_winner())

    def testGetWinnerNone1(self):
        dims = {
            (1, 1),
            (3, 3),
            (2, 5),
        }
        for nrows, ncols in dims:
            with self.subTest(f"{nrows}, {ncols}"):
                # Blank board has no winner
                board = self.GAME_BOARD_TYPE(nrows, nrows)
                self.assertEqual(GameBoardPlayer.NONE, board.get_winner())

    def testGetWinnerNone2(self):
        dims = {
            (3, 3),
            (2, 5),
        }
        for nrows, ncols in dims:
            for row in range(nrows):
                for col in range(ncols):
                    with self.subTest(f"{nrows}, {ncols}, {row}, {col}"):
                        # Blank board with one space set has no winner
                        board = self.GAME_BOARD_TYPE(nrows, ncols)
                        board.set(row, col, GameBoardPlayer.X)
                        self.assertEqual(GameBoardPlayer.NONE, board.get_winner())

    def testGetWinnerNone3(self):
        board = self.helpMakeBoardWithDraw()
        for row in range(board.get_nrows()):
            for col in range(board.get_ncols()):
                with self.subTest(f"{row}, {col}"):
                    # A DRAW board with one space set to NONE has no winner
                    board_copy = copy.deepcopy(board)
                    board_copy.set(row, col, GameBoardPlayer.NONE)
                    self.assertEqual(GameBoardPlayer.NONE, board_copy.get_winner(), "\n" + str(board_copy))

    def testGetAllMoves(self):
        # board is empty
        board = self.GAME_BOARD_TYPE(3, 3)
        expected = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1),
                    (1, 2), (2, 0), (2, 1), (2, 2)]
        actual = board.get_all_moves()
        self.assertEqual(expected, actual)

        #occupying some spaces...
        board.set(1, 0, GameBoardPlayer.X)
        board.set(1, 1, GameBoardPlayer.O)
        board.set(1, 2, GameBoardPlayer.X)
        board.set(2, 0, GameBoardPlayer.O)
        board.set(2, 1, GameBoardPlayer.X)

        expected = [(0, 0), (0, 1), (0, 2), (2, 2)]
        actual = board.get_all_moves()
        self.assertEqual(expected, actual)

        #occupying remaining spaces
        board.set(0, 0, GameBoardPlayer.X)
        board.set(0, 1, GameBoardPlayer.X)
        board.set(0, 2, GameBoardPlayer.O)
        board.set(2, 2, GameBoardPlayer.X)

        expected = []       #expect empty list
        actual = board.get_all_moves()
        self.assertEqual(expected, actual)





class ArrayGameBoardTestCase(GameBoardTestCase):
    GAME_BOARD_TYPE = ArrayGameBoard


class BitGameBoardTestCase(GameBoardTestCase):
    GAME_BOARD_TYPE = BitGameBoard


class AiPlayerTestCase(unittest.TestCase):
    def testAiSetMove(self):
        ai_player = AiPlayer(GameBoardPlayer.X)
        ai_opponent = AiPlayer(GameBoardPlayer.O)
        board = TicTacToeBoard()
        #ttt_game(ai_player, ai_opponent)

        board.set(1, 1, GameBoardPlayer.O)
        board.set(0, 0, GameBoardPlayer.X)
        board.set(2, 2, GameBoardPlayer.O)
        board.set(0, 2, GameBoardPlayer.X)
        board.set(2, 0, GameBoardPlayer.O)

        expected = (0, 1)
        actual = row, col = ai_player.get_move(copy.deepcopy(board))
        self.assertEqual(expected, actual)

    def testAiSetMove2(self):
        ai_player = AiPlayer(GameBoardPlayer.X)
        ai_opponent = AiPlayer(GameBoardPlayer.O)
        board = TicTacToeBoard()
        #ttt_game(ai_player, ai_opponent)

        board.set(0, 0, GameBoardPlayer.O)
        board.set(1, 1, GameBoardPlayer.X)
        board.set(0, 2, GameBoardPlayer.O)
        board.set(0, 1, GameBoardPlayer.X)
        board.set(2, 2, GameBoardPlayer.O)

        expected = (2, 1)
        actual = row, col = ai_player.get_move(copy.deepcopy(board))
        self.assertEqual(expected, actual)

    def testAiSetMove3(self):
        ai_player = AiPlayer(GameBoardPlayer.X)
        ai_opponent = AiPlayer(GameBoardPlayer.O)
        board = TicTacToeBoard()
        #ttt_game(ai_player, ai_opponent)

        board.set(1, 1, GameBoardPlayer.O)
        board.set(0, 0, GameBoardPlayer.X)
        board.set(0, 2, GameBoardPlayer.O)
        board.set(2, 0, GameBoardPlayer.X)
        board.set(1, 0, GameBoardPlayer.O)
        board.set(1, 2, GameBoardPlayer.X)
        board.set(0, 1, GameBoardPlayer.O)

        expected = (2, 1)
        actual = row, col = ai_player.get_move(copy.deepcopy(board))
        self.assertEqual(expected, actual)







# Remove the class so its tests won't run and fail
# https://stackoverflow.com/questions/4566910/abstract-test-case-using-python-unittest
del GameBoardTestCase

if __name__ == '__main__':
    unittest.main()
