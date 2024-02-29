import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if all([board[i][j] == "X" for j in range(3)]) or \
           all([board[j][i] == "X" for j in range(3)]):
            return "X"
        elif all([board[i][j] == "O" for j in range(3)]) or \
             all([board[j][i] == "O" for j in range(3)]):
            return "O"
    if all([board[i][i] == "X" for i in range(3)]) or \
       all([board[i][2-i] == "X" for i in range(3)]):
        return "X"
    elif all([board[i][i] == "O" for i in range(3)]) or \
         all([board[i][2-i] == "O" for i in range(3)]):
        return "O"
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner is not None:
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        else:
            return 0

    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("This cell is already occupied. Try again.")
            continue

        board[row][col] = "X"

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print("Computer's turn...")
        best_move = get_best_move(board)
        board[best_move[0]][best_move[1]] = "O"

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

tic_tac_toe()
