from random import randint

# The board
board = [["*","*","*"],
         ["*","*","*"],
         ["*","*","*"]]

# function which prints out the board
def pretty_print():
    for row in board:
        print(*row)

# Function that takes the user's place and value and puts it on the board
def take_input(player_token):
    # Main variables
    row = int(input(f"Row to place the {player_token}: "))
    column = int(input(f"Column to place the {player_token}: "))

    # Validation

    if row in range(1,4) and column in range(1,4):
        if board[row-1][column-1] != "*":
            print("This spot is taken")
            take_input(player_token)
        else:
            board[row-1][column-1] = player_token
    else:
        print("Something went wrong, try again")
        take_input(player_token)

def check_win_in_rows(board, token):
    for row in board:
        check_row = True
        for element in row:
            if element != token:
                check_row = False
        if check_row:
            return True
    return False

def check_win_in_columns(board, token):
    for column in range(len(board)):
        check_column = True
        for row in range(len(board)):
            if board[row][column] != token:
                check_column = False
        if check_column:
            return True
    return False

def check_win_in_main_diagonal(board, token):
    if board[0][0] != token or board[1][1] != token or board[2][2] != token:
        return False
    else:
        return True

def check_win_in_secondary_diagonal(board, token):
    if board[2][0] != token or board[1][1] != token or board[0][2] != token:
        return False
    else:
        return True

steps = 0
pretty_print()
while True:
    if steps % 2 == 0:
        take_input("x")
    else:
        take_input("o")
    steps += 1
    pretty_print()

    if steps > 4:
        if check_win_in_rows(board, "x") or check_win_in_columns(board, "x") or check_win_in_main_diagonal(board, "x") or check_win_in_secondary_diagonal(board, "x"):
            print("Player X wins!")
            break
        if check_win_in_rows(board, "o") or check_win_in_columns(board, "o") or check_win_in_main_diagonal(board, "o") or check_win_in_secondary_diagonal(board, "o"):
            print("Player O wins!")
            break
    if steps == 9:
        print("It's a draw!")
        break