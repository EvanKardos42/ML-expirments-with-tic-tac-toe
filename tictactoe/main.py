from tictactoe.GameBoard import Game_Board
from tictactoe.AI import Robot


def play_game(bob):
    player1,player2 = "X", "O"
    turn_tracker = 0
    current_player = player1
    game_over = False
    game: Game_Board = Game_Board()

    while not game_over:
        if turn_tracker % 2 == 0:
            current_player = player1
            player_move = bob.move(game.board, turn_tracker)
            print("computer\'s move")
        else:
            # print("turn count {}".format(turn_tracker))
            current_player = player2
            player_move = int(input("input a number: ")) - 1

        game.play_move(player_move, current_player)

        if game.check_winner():
            game_over = True
        elif game.board_full():
            current_player = " "
            game_over = True
        print(game.get_printable_board())
        turn_tracker += 1

    print(game.get_printable_board())
    return current_player


if __name__ == "__main__":
    bob = Robot()
    result = play_game(bob)
    if result == " ":
        print("its a tie")
    else:
        print("the winner is " + result + "s")
