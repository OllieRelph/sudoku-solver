def check_valid(coord_dict,puzzle):
    '''
    coord_dict -> Dictionary: contains key 'x' and 'y' containing x, y position to check for valid values
    puzzle -> 2D List: Full puzzle with current solved values

    returns -> List: possible values
    '''
    row_vals = check_row_valid(coord_dict,puzzle)
    col_vals = check_column_valid(coord_dict,puzzle)
    box_vals = check_box_valid(coord_dict,puzzle)
    vals = [1,2,3,4,5,6,7,8,9]
    possible_vals = []
    for val in vals:
        if val in row_vals:
            if val in col_vals:
                if val in box_vals:
                    possible_vals.append(val)      
    return possible_vals

def check_row_valid(coord_dict,puzzle):
    '''
    coord_dict -> Dictionary: contains key 'x' and 'y' containing x, y position to check for valid values
    puzzle -> 2D List: Full puzzle with current solved values

    returns -> List: possible values
    '''
    #initialises possible list
    valid_list = [1,2,3,4,5,6,7,8,9]
    row_num = coord_dict.get('y')
    #reads across the row of the coord and removes all values seen
    for item in puzzle[row_num][:]:
        if item in valid_list:
            valid_list.remove(item)
    return valid_list

def check_column_valid(coord_dict,puzzle):
    '''
    coord_dict -> Dictionary: contains key 'x' and 'y' containing x, y position to check for valid values
    puzzle -> 2D List: Full puzzle with current solved values

    returns -> List: possible values
    '''
    #initialise possible list
    valid_list = [1,2,3,4,5,6,7,8,9]
    column_num = coord_dict.get('x')
    #reads across the column of the coord and removes all values seen
    for item in [row[column_num] for row in puzzle]:
        if item in valid_list:
            valid_list.remove(item)
    return valid_list

def get_box_range(coord_dict):
    '''
    coord_dict -> Dictionary: keys 'x' and 'y' containing coordinate checking, calculates its box

    returns -> Dictionary keys 'x_range' and 'y_range'

    '''
    row_num = coord_dict.get('y')
    column_num = coord_dict.get('x')
    if row_num in [0,1,2]:
        row_range = [0,1,2]
    elif row_num in [3,4,5]:
        row_range = [3,4,5]
    else:
        row_range = [6,7,8]

    if column_num in [0,1,2]:
        column_range = [0,1,2]
    elif column_num in [3,4,5]:
        column_range = [3,4,5]
    else:
        column_range = [6,7,8]
    
    return {'y_range':row_range,
            'x_range':column_range}

def check_box_valid(coord_dict,puzzle):
    '''
    coord_dict -> Dictionary: keys 'x' and 'y' containing coordinate checking, calculates its box
    puzzle -> currently solved puzzle

    returns -> Dictionary keys 'x_range' and 'y_range'

    '''
    valid_list = [1,2,3,4,5,6,7,8,9]
    box_range = get_box_range(coord_dict)
    x_range = box_range.get('x_range')
    y_range = box_range.get('y_range')
    for col in x_range:
        for row in y_range:
            if puzzle[row][col] in valid_list:
                valid_list.remove(puzzle[row][col])
    return valid_list
    
    
    


    
    
    