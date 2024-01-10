# N Queens Problem Solver
## Description
This program solves the N Queens puzzle, which involves placing N non-attacking queens on an N×N chessboard. The program finds and prints every possible solution to the problem for a given board size.

## Usage
To run the program, use the following command:
```
./0-nqueens.py N
```
`N`: The size of the board and the number of queens.
## Examples
For a 4x4 board:
```
./0-nqueens.py 4
```
Output:
```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
For a 6x6 board:
```
./0-nqueens.py 6
```
Output:
```
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
## Approach
The program utilizes backtracking to place queens on the board, ensuring that no two queens attack each other. It checks for the validity of a queen placement in terms of rows, columns, and diagonals.