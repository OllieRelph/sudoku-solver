# sudoku-solver
Solves sudoku puzzle stored in config.yaml

currently solves by calculating possible values for any cell, filling in cells that have 1 possible value.

further efficiency and difficulty needs to include backtracking, once there are no cells with only 1 possible value we need to try a value in 1 and keep running, if valid then continue, if we reach an invalid cell then we backtrack to last filled cell with multiple choices and backtrack
