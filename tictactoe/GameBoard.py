class Rules:

    def __init__(self):
        self._rows = 3
        self._cols = 3

    # returns a string representation
    # of the current board
    def get_printable_board(self, list_board=[1]):
        if len(list_board) == 9:
            return " " + list_board[0] + " | " + list_board[1] + " | " + list_board[2] + "\n" + \
                   "------------\n" + \
                   " " + list_board[3] + " | " + list_board[4] + " | " + list_board[5] + "\n" + \
                   "------------\n" + \
                   " " + list_board[6] + " | " + list_board[7] + " | " + list_board[8] + "\n"
        else:
            print("error, board need to be 9, length is " + str(len(list_board)))

    # allows the user to make a move on the board
    def play_move(self, player_input, player_symbol, list_board):
        if list_board[player_input] not in ['X', 'O']:
            list_board[player_input] = player_symbol
            return True
        else:
            return False

    # checks to see if the board has a winner
    # returns boolean, string
    def check_winner(self, list_board: list):
        # checks rows
        for i in range(self._rows):
            if list_board[i] == list_board[i + 1] == list_board[i + 2]:
                return True
        # checks the columns
        for i in range(self._cols):
            if list_board[i] == list_board[i + 3] == list_board[i + 6]:
                return True

        # checks the diagonals
        if list_board[0] == list_board[4] == list_board[8]:
            return True
        elif list_board[2] == list_board[4] == list_board[6]:
            return True
        else:
            return False

    def board_full(self, board):
        count = 0
        for i in board:
            if i in ['X', 'O']:
                count += 1
        return count == 9
