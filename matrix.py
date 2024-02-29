# Define the game state
game_state = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

# Define the player and opponent
player = 1
opponent = 2

# Function to check if the game is over
def is_game_over(state):
    # Check rows
    for row in state:
        if row.count(1) == 3 or row.count(2) == 3:
            return True

    # Check columns
    for col in range(3):
        if state[0][col] == state[1][col] == state[2][col] != 0:
            return True

    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2] != 0 or \
       state[0][2] == state[1][1] == state[2][0] != 0:
        return True

    return False

# Function to evaluate the game state
def evaluate(state):
    # Check rows
    for row in state:
        if row.count(1) == 3:
            return 10
        elif row.count(2) == 3:
            return -10

    # Check columns
    for col in range(3):
        if state[0][col] == state[1][col] == state[2][col] == 1:
            return 10
        elif state[0][col] == state[1][col] == state[2][col] == 2:
            return -10

    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2] == 1 or \
       state[0][2] == state[1][1] == state[2][0] == 1:
        return 10
    elif state[0][0] == state[1][1] == state[2][2] == 2 or \
         state[0][2] == state[1][1] == state[2][0] == 2:
        return -10

    # If no winner yet
    return 0

# Function to check if there are any moves left
def is_moves_left(state):
    for row in state:
        for val in row:
            if val == 0:
                return True
    return False

# Function to find the optimal move
def minimax(state, depth, is_max):
    score = evaluate(state)

    if score == 10:
        return score

    if score == -10:
        return score

    if not is_moves_left(state):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = player
                    best = max(best, minimax(state, depth + 1, not is_max))
                    state[i][j] = 0
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = opponent
                    best = min(best, minimax(state, depth + 1, not is_max))
                    state[i][j] = 0
        return best

# Main part - find the best move
best_val = -1000
best_move = (-1, -1)

for i in range(3):
    for j in range(3):
        if game_state[i][j] == 0:
            game_state[i][j] = player
            move_val = minimax(game_state, 0, False)
            game_state[i][j] = 0
            if move_val > best_val:
                best_move = (i, j)
                best_val = move_val

print("The optimal move is:", best_move)

