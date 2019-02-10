from tictactoe.GameBoard import Game_Board


class Robot:
    def __init__(self):
        self.rules = Game_Board()
        self.symbol = "X"
        self.opponent = "O"

    def move(self, board: list, turn):
        if turn == 0:
            return 4
        else:
            return self._recurse_find_move(board.copy() , self.symbol)

    def _recurse_find_move(self, current_state: list, current_player, move=0):
        """a simple recursion algorithm that will find the first best move
         that will win the game
         :returns a number with the first end game move"""

        self.rules.play_move(move, current_player, current_state)
        score = self._score_board(current_state, current_player)

        if score != 0:  # found either a good move(1) or bad move (-1)
            return score
        else:
            for place in range(0, 9):
                if current_state[place] not in ["X", "O"]:
                    m = self._recurse_find_move(current_state.copy(),
                                                self._check_turn(current_player),
                                                place)
                    if m == -1:
                        # undo the move
                        current_state[place] = str(place + 1)
                    else:
                        return place

    # checks to see if the current state is a good move
    def _score_board(self, board_state: list, winner):
        """ checks to see if the board state is a win result
            :returns 1 if it is a favorable move
            :returns -1 if it is not a favorable move
            :returns 0 others"""
        ended = self.rules.check_winner(board_state)
        tied = self.rules.board_full(board_state)
        if ended and winner == self.symbol or tied:
            return 10
        elif ended and winner == self.opponent:
            return -10
        else:
            return 0

    def _check_turn(self, symbol):
        """ tell the computer who turn will be next
            given the current symbol
            :returns the other players symbol"""
        if symbol == self.symbol:
            return self.opponent
        else:
            return self.symbol
