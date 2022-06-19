import yaml
import os
from check_valid import check_valid


#set current file path directory
current_py_dir = os.path.dirname(os.path.abspath(__file__))
# Read YAML config file
with open(current_py_dir + '/config/config.yaml', 'r') as stream:
    config = yaml.safe_load(stream)
# Config params
sudoku_puzzles = config['input']


sudoku_vals = [item for sublist in sudoku_puzzles for item in sublist]
while 0 in sudoku_vals:
    for x in range(0,9):
        for y in range(0,9):
            if sudoku_puzzles[y][x] == 0:
                # print(f'row: {y} and column: {x}')
                valid_vals = check_valid({'x':x,'y':y}, sudoku_puzzles)
                if len(valid_vals) == 1:
                    sudoku_puzzles[y][x] = valid_vals[0]
    sudoku_vals = [item for sublist in sudoku_puzzles for item in sublist]
print(sudoku_puzzles)
