# This is a Python script for developing the game Tic Tac Toe

# Game Board
empty_board = ["-", "-", "-",
               "-", "-", "-",
               "-", "-", "-"]

# If game is still going on
game_is_still_going = True

# Who won the game or is it a tie?
winner = None

# Whose turn is it?
current_player = "X"


def display_empty_board():
    print(empty_board[0] + " | " + empty_board[1] + " | " + empty_board[2])
    print(empty_board[3] + " | " + empty_board[4] + " | " + empty_board[5])
    print(empty_board[6] + " | " + empty_board[7] + " | " + empty_board[8])


def handle_turn():
    # By default the input functions takes the keyempty_board input as strings
    position = input("Choose a position from 1 to 9: ")
    # Change the input to integer type and deduct 1 to make the value start from 0 to 8
    position = int(position) - 1
    empty_board[position] = "X"
    print("Here is the current status of the empty_board:")
    display_empty_board()


def check_if_win():
    # check the rows
    # check the columns
    # check the diagonals
    return


def check_if_tie():
    # check the rows
    # check the columns
    # check the diagonals
    return


def check_if_game_is_over():
    check_if_win()
    check_if_tie()


def flip_player():
    return


def PlayGame():
    # Display initial empty_board
    display_empty_board()
    while game_is_still_going:
        handle_turn(current_player)
        check_if_game_is_over()
        flip_player()


PlayGame()
