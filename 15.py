import sys

# Define constants for players
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

# Define constants for evaluation
SCORES = {
    PLAYER_X: 1,
    PLAYER_O: -1,
    EMPTY: 0
}

# Define the initial state of the board
initial_board = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]


def print_board(board):
    for row in board:
        print(" | ".join(map(lambda x: "X" if x == PLAYER_X else "O" if x == PLAYER_O else " ", row)))
        print("---------")


def evaluate(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return SCORES[board[i][0]]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return SCORES[board[0][i]]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return SCORES[board[0][0]]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return SCORES[board[0][2]]

    return SCORES[EMPTY]


def is_terminal_node(board):
    return evaluate(board) != SCORES[EMPTY] or not any(EMPTY in row for row in board)


def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves


def minimax(board, depth, maximizing_player):
    if is_terminal_node(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -sys.maxsize
        for move in get_available_moves(board):
            board[move[0]][move[1]] = PLAYER_X
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for move in get_available_moves(board):
            board[move[0]][move[1]] = PLAYER_O
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval


def get_best_move(board):
    best_move = None
    best_eval = -sys.maxsize
    for move in get_available_moves(board):
        board[move[0]][move[1]] = PLAYER_X
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def play_game():
    board = initial_board
    current_player = PLAYER_X

    while not is_terminal_node(board):
        print_board(board)
        if current_player == PLAYER_X:
            row, col = map(int, input("Enter row and column (0-2) for X: ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                current_player = PLAYER_O
            else:
                print("Invalid move. Try again.")
        else:
            print("Computer is making a move...")
            row, col = get_best_move(board)
            board[row][col] = PLAYER_O
            current_player = PLAYER_X

    print_board(board)
    winner = evaluate(board)
    if winner == SCORES[PLAYER_X]:
        print("X wins!")
    elif winner == SCORES[PLAYER_O]:
        print("O wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()
