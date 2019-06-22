# Daily Coding 38
# You have an N by N board. Write a function that, given N, returns the number of possible
# arrangements of the board where N queens can be placed on the board without threatening each other
# i.e. no two queens share the same row, column, or diagonal.

def is_valid(board, row):
    if row in board:
        return False
    col = len(board)
    for b_col, b_row in enumerate(board):
        if abs(b_row - row) == abs(b_col - col):
            return False
    return True

def get_queens_positions(board, n):
    if n == len(board):
        return 1
    count = 0
    for row in range(n):
        if is_valid(board, row):
            count += get_queens_positions(board + [row], n)
    return count

def n_queens(n):
    return get_queens_positions([], n)

print(n_queens(8))