
# 🔢Terminal-Based Sudoku Solver🔷

This Sudoku Solver is a Python-based program that generates random Sudoku puzzles, displays them in the terminal with colorful formatting, solves the puzzles using recursion and backtracking, and finally, displays the solved Sudoku grids.

![Sodoku img Screenshot](https://github.com/amit-singh-coding/Terminal-Based-Sudoku-solver/blob/main/sudoku_img.jpg)


## Specifications:

**Input:** 

1- Size of the Sudoku puzzle (9).

2- Users choose to either print the solved puzzle, generate another puzzle, or exit the game.


**Outpur:**

1- A visual representation of the generated Sudoku puzzle in the terminal.

2- A visual representation of the solved Sudoku puzzle in the terminal.

+ Empty cells: White background
+ Unsolved cells: sky-blue text
+ Initial puzzle values: black text
+ Solved cells: Green text




## Prerequisites

- Basic understanding of arrays and loops.

- Familiarity with terminal-based input/output.


## Code Components

**Libraries**

🎲 random : Used for generating random numbers for maze generation.

🖥️ os: Used for clearing the terminal screen ('cls' for Windows, 'clear' for Unix-like systems).

**Data Structures Used**

`Stack :` Used in the Recursive Backtracking puzzle generation algorithm.

`2D List :` Used for storing generated sudoku puzzel

`List :` Used for storing the solution path.


**Algorithms**

+ Recursion

+ backtracking
## Installation

1- Clone the repository: `git clone https://github.com/amit-singh-coding/Terminal-Based-Sudoku-solver`

2- Navigate to the project directory: `cd Terminal-Based-Sudoku-solver`

3- Run the program: `python sudoku_solver.py` 

4- Install dependencies: `pip install -r requirements.txt`

## Contributions
Contributions are welcome! If you find any issues or have improvements in mind, feel free to submit a pull request.

## License
This Sudoku Solver is licensed under the `MIT License`.

