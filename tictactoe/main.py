from tictactoe.GameBoard import Rules
from tictactoe.AI import Robot


def play_game(bob):
    board_grid = [str(i) for i in range(1, 10)]
    player1 = "X"
    player2 = "O"
    turn_tracker = 0
    current_player = player1
    game_over = False
    rule_book: Rules = Rules()
    player_move = int(0)

    while not game_over:
        if turn_tracker % 2 == 0:
            current_player = player1
            player_move = bob.move(board_grid, turn_tracker)
        else:
            print(rule_book.get_printable_board(board_grid))
            # print("turn count {}".format(turn_tracker))
            current_player = player2
            player_move = int(input("input a number: ")) - 1

        rule_book.play_move(player_move, current_player, board_grid)

        if rule_book.check_winner(board_grid):
            game_over = True
        elif rule_book.board_full(board_grid):
            current_player = " "
            game_over = True

        turn_tracker += 1

    print(rule_book.get_printable_board(board_grid))
    return current_player


if __name__ == "__main__":
    bob = Robot()
    result = play_game(bob)
    if result == " ":
        print("its a tie")
    else:
        print("the winner is " + result + "s")
