# Write you solution here
empty = 0
player_1 = 1
player_2 = 2
players = {0: " ",
           1: "X",
           2: "O"}


def make_game_board(n=3):
    return [[empty] * n for i in range(n)]


# return 1 if p1 wins
# return 2 if p2 wins
# return 0 if game not finished
# return -1 if draw
def check_game_finished(board):
    board_wins = [row for row in board]
    board_wins += [list(row) for row in zip(*board)]
    board_wins += [[board[i][i] for i in range(len(board))]]
    board_wins += [[board[len(board) - 1 - i][i] for i in range(len(board))]]
    if [1] * len(board) in board_wins:
        return 1
    elif [2] * len(board) in board_wins:
        return 2
    elif True in [board[i][j] == 0 for i in range(len(board)) for j in range(len(board))]:
        return 0
    else:
        return -1


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def draw_game_board(board):
    top = "   "
    for col in range(1, len(board) + 1):
        top += " " + str(col) + "  "
    print(top)
    r = 0
    for row in board:
        line_1 = "  "
        line_2 = alphabet[r] + " "
        r += 1
        for col in row:
            line_1 += " ---"
            line_2 += "| " + players[col] + " "
        line_2 += "|"
        print(line_1)
        print(line_2)
    print("  " + " ---" * len(board))


def _move(board, player, coordinates):
    x, y = coordinates
    if board[x][y] == 0:
        board[x][y] = player
        return True
    else:
        return False


def move(board, player, location):
    row = alphabet.find(location[0])
    col = int(location[1:]) - 1
    if board[row][col] == 0:
        _move(board, player, (row, col))
        return True
    else:
        print("Cannot put " + players[player] + " at location " + location)
        return False


def player_move(board, player):
    location = "A1"
    while True:
        draw_game_board(board)
        location = input("Place " + players[player] + " at: ").upper()
        if location[0] in alphabet and alphabet.find(location[0]) < len(board) and location[1:].isnumeric() and 0 < int(
                location[1:]) <= len(board) <= 26:
            break
        else:
            print("Invalid location. Try again.")
    if move(board, player, location):
        return True
    else:
        return player_move(board, player)


def tic_tac_toe():
    while True:
        board = make_game_board()
        current_player = True
        while check_game_finished(board) == 0:
            if current_player:
                player_move(board, 1)
            else:
                player_move(board, 2)
            current_player = not current_player
        result = check_game_finished(board)
        draw_game_board(board)
        print("It's a draw!" if result == -1 else ("Player 1 wins!" if result == 1 else "Player 2 wins!"))


tic_tac_toe()
