import unittest as test_frames
from tictactoe.AI import Robot
from tictactoe.GameBoard import Game_board


class MyTest(test_frames.TestCase):

    def setUp(self):
        self.rules = Game_board()

    def test_check_winner(self):
        board = ["X", "X", "X",
                 "O", "O", "6",
                 "O", "O", "X"]
        r = Game_board()
        # test the rows
        answer = r.check_winner(board)
        self.assertEqual(True, answer, "class did not find that X's should have won")

        # test the columns
        board = ["O", "X", "X",
                 "O", "X", "O",
                 "O", "8", "O"]
        answer = r.check_winner(board)
        self.assertEqual(True, answer, "class did not find that O's should have won")
        # test the diagonals

    """All AI test check to see if the algorithm
        makes the correct move on the array
        if the best move is position 5 then the robot 
        should make move on index 4"""

    def test_AI_1(self):
        board = ["X", "O", "X",
                 "X", "O", "O",
                 "7", "8", "9"]
        bob = Robot()
        answer = bob.move(board, 7)
        self.assertEqual(6, answer, "test 1: did not find the best move to win\n"

                         + self.rules.get_printable_board(board))

    def test_AI_2(self):
        board = ["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]
        bob = Robot()
        answer = bob.move(board, 0)
        self.assertEqual(4, answer, "test 2: did not move in the center\n"
                         + self.rules.get_printable_board(board))

    def test_AI_3(self):
        board = ["O", "2", "X",
                 "4", "5", "6",
                 "O", "8", "X"]
        bob = Robot()
        answer = bob.move(board, 1)
        self.assertEqual(5, answer, "test 3: did place in position 6\n"
                         + self.rules.get_printable_board(board))

    def test_AI_4(self):
        board = ["O", "2", "3",
                 "O", "X", "6",
                 "7", "8", "9"]
        bob = Robot()
        answer = bob.move(board, 1)
        self.assertEqual(6, answer, "test 4: did not block O\'s \n"
                         + self.rules.get_printable_board(board))
