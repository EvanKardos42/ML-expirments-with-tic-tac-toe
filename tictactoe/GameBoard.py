class Game_Board:

    def __init__(self, board =[str(i) for i in range(1,10)] ):
        self.board = board
        self._rows = 3
        self._cols = 3

    # returns a string representation
    # of the current board
    def get_printable_board(self,):
        return " " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "\n" + \
                   "------------\n" + \
                   " " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "\n" + \
                   "------------\n" + \
                   " " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "\n"

    # allows the user to make a move on the board
    def play_move(self, player_input, player_symbol, board = None):
        if board is None:
            if self.board[player_input] not in ['X', 'O']:
                self.board[player_input] = player_symbol
                return True
            else:
                return False
        else:
            if board[player_input] not in ['X', 'O']:
                board[player_input] = player_symbol
                return True
            return False


    # checks to see if the board has a winner
    # returns boolean, string
    def check_winner(self,board=None):
        # checks rows
        if board is None:
            for i in range(self._rows):
                if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                    return True
            # checks the columns
            for i in range(self._cols):
                if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                    return True

            # checks the diagonals
            if self.board[0] == self.board[4] == self.board[8]:
                return True
            elif self.board[2] == self.board[4] == self.board[6]:
                return True
            else:
                return False
        else:
            #check rows
            for i in range(self._rows):
                if board[i] == board[i + 1] == board[i + 2]:
                    return True
            # checks the columns
            for i in range(self._cols):
                if board[i] == board[i + 3] == board[i + 6]:
                    return True

            # checks the diagonals
            if board[0] == board[4] == board[8]:
                return True
            elif board[2] == board[4] == board[6]:
                return True
            else:
                return False



    def board_full(self, board = None):
        count = 0
        if board is not None:
            for i in board:
                if i in ['X', 'O']:
                    count += 1
            return count == 9
        else:
            for i in self.board:
                if i in ['X', 'O']:
                    count += 1
            return count == 9
