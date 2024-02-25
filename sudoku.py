import random
def generate_sudoku(size):
    # Create an empty Sudoku grid---------------
    grid = [[0] * size for _ in range(size)]

    # Generate a solved Sudoku grid-------------
    solve_sudoku(grid)

    # Remove random cells to create the puzzle--
    remove_cells(grid, size)

    return grid

def is_valid_move(grid, row, col, num, size):
    # Check if the number is not in the same row or column
    if num in grid[row] or num in [grid[i][col] for i in range(size)]:
        return False

    # Check if the number is not in the same 3x3 block
    block_size = int(size**0.5)
    start_row, start_col = row - row % block_size, col - col % block_size

    for i in range(block_size):
        for j in range(block_size):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 0:
                # Try filling the cell with a valid number
                for num in range(1, size + 1):
                    if is_valid_move(grid, row, col, num, size):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack if the solution is not valid
                return False
    return True

def remove_cells(grid, size):
    # Remove random cells to create the puzzle
    num_cells_to_remove = size**2 // 2

    for _ in range(num_cells_to_remove):
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[row][col] = 0

#solve the sudoku---------------------------------------------
def is_possible(mat,r,c,ch):
    for i in range(0,9): #--->check for row
        if mat[r][i]==ch:
            return False
        if mat[i][c]==ch:#-->check for column
            return False
    #--->check for 3X3 box
    box_r=(r//3)*3
    box_c=(c//3)*3
    for i in range(box_r,box_r+3): 
        for j in range(box_c,box_c+3):
            if mat[i][j]==ch:
                return False
    return True            
def solve(mat,r,c):
    if r==9:
        return True
    if c==9:
        return solve(mat,r+1,0)
        
    if mat[r][c]!=0:
        return solve(mat,r,c+1)
    for ch in range(1,10):
        if is_possible(mat,r,c,ch):
            mat[r][c]=ch
            if solve(mat,r,c+1):
                return True
            else:    
                mat[r][c]=0
    return False                        


# Print the generated Sudoku puzzle====================================?
class BackgroundColor:
    WHITE = '\033[48;5;15m'
    GREEN = '\033[48;5;32m'
    GG = '\033[48;5;46m'
    SKY_BLUE = '\033[48;5;39m'
    END = '\033[0m'  # Reset background color to default


def print_G_sudoku(sudoku_grid): 
    zero_list=[]         
    for r in range(9):
        for c in range(9):
            if sudoku_grid[r][c] == 0:
                zero_list.append([r,c])
                x3 = f"{BackgroundColor.SKY_BLUE} {0} {BackgroundColor.END}"
                print(x3, end=" ")
            else:
                x1 = f"{BackgroundColor.WHITE} {sudoku_grid[r][c]} {BackgroundColor.END}"
                print(x1, end=" ")
        print()
    return zero_list     

# Print the solved Sudoku puzzle====================================?                  
def print_solved_sudoku(sudoku_grid, track_zero):      
    for r in range(9):
        for c in range(9):
            if [r,c] in track_zero:               
                x3 = f"{BackgroundColor.GG} {sudoku_grid[r][c]} {BackgroundColor.END}"
                print(x3, end=" ")
            else:
                x1 = f"{BackgroundColor.WHITE} {sudoku_grid[r][c]} {BackgroundColor.END}"
                print(x1, end=" ")
        print()    

while True:
    user_input2=int(input("""
      1. Generate New puzzle
      2. Print & solve the sudoku
      3. Exit the Game
      Enter your choice (1/2/3): """))
    if user_input2==1:
        sudoku_grid = generate_sudoku(9)
        # Print the generated sudoku--------------
        track_zero=print_G_sudoku(sudoku_grid)
        print("🟢-Sudoku generated----")                          
    elif user_input2==2:
        try:    
            n=len(sudoku_grid)
            if_possiblde_to_solve = solve(sudoku_grid,0,0)
            if if_possiblde_to_solve :
                print_solved_sudoku(sudoku_grid,track_zero)     
                print("------------------------------------------------------------------------------")    
            else:
                print("NOTE POSSIBLE TO SOLVE----")  
        except:
            print("🔴-First Generate The Sudoku------------")  
    else:
        print("🟢-Thanks You--")
        break     
