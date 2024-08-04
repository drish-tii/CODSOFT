import math
import random

# Define constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Define the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, PLAYER_X):
        return 10 - depth
    if is_winner(board, PLAYER_O):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for (i, j) in available_moves(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (i, j) in available_moves(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    move = None
    best_value = -math.inf
    for (i, j) in available_moves(board):
        board[i][j] = PLAYER_X
        move_value = minimax(board, 0, -math.inf, math.inf, False)
        board[i][j] = EMPTY
        if move_value > best_value:
            best_value = move_value
            move = (i, j)
    return move

def main():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        # Player X's move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = PLAYER_X
            print("AI (X) played:")
            print_board(board)
            if is_winner(board, PLAYER_X):
                print("AI (X) wins!")
                break
            if is_full(board):
                print("It's a draw!")
                break

        # Player O's move (human)
        if not is_full(board) and not is_winner(board, PLAYER_X):
            move = None
            while move not in available_moves(board):
                try:
                    move = tuple(map(int, input("Enter your move (row and column): ").split()))
                except:
                    pass
            board[move[0]][move[1]] = PLAYER_O
            print("Player (O) played:")
            print_board(board)
            if is_winner(board, PLAYER_O):
                print("Player (O) wins!")
                break
            if is_full(board):
                print("It's a draw!")
                break

if __name__ == "__main__":
    main()
