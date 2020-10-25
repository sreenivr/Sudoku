board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 2, 0, 7, 0],
    [0, 0, 0, 0, 1, 3, 2, 8, 0],
    [8, 0, 0, 9, 0, 6, 0, 4, 0],
    [7, 0, 1, 0, 0, 0, 0, 2, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 8, 0, 0, 0, 0, 5, 3, 7],
    [0, 0, 0, 5, 6, 0, 0, 0, 4],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],    
]

# print the sudoku board
def print_board():
    for i in range(len(board)):
        if ((i % 3) == 0) and (i != 0):
            print("- - - - - - - - - -")
        for j in range(len(board[i])):
            if ((j % 3) == 0) and (j != 0):
                print("|", end="")
            print (board[i][j], "", end='')
        print()

# Check if the given number is valid at the location specified at the row(r), col(c) on the board(b)
def is_allowed(r, c, num):
    if num > 9 or num < 1 or r > 9 or r < 0 or c > 9 or c < 0: 
        raise Exception("check_valid(): only numbers 1-9 are allowed.")
        return False
    # Check if the the given num in col
    for i in range(9):
        if(board[i][c] == num):
            return False
    # Check if the the given num in row
    for i in range(9):
        if(board[r][i] == num):
            return False
    # Check if the num in 3x3 grid
    gr = r // 3
    gc = c // 3
    for i in range(gr*3, gr*3 + 3):
        for j in range(gc*3, gc*3 + 3):
            #print(i, j, board[i][j])
            if board[i][j] == num:
                return False
    return True

# Check if all the 9x9 locations are filled
def is_empty():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return True
    return False


# Recursive function to solve the Sudoku
def solve():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    allowed = is_allowed(row, col, num)
                    if allowed:
                        board[row][col] = num
                        solve()
                        if (is_empty() is False): return
                        board[row][col] = 0
                return

def run(b):
    global board
    board = b
    solve()
                
if __name__ == '__main__':
    # Example board
    b = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]
    run(b)
    print_board()
   