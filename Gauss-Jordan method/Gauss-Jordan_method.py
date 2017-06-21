from copy import deepcopy


def JG(matrix, index_row, index_col):
    fix_point = 2
    # check_sum = 0
    width = len(matrix[0])
    height = len(matrix)
    res = deepcopy(matrix)
    variable_count = width - 1  # skip free element
    if index_row < height and index_col < variable_count:
        x = matrix[index_row][index_col]
        # Choosing may be the solving element equal 0.
        if x == 0:
            # Find first not 0 element and set it to solving element.
            for i in range(variable_count):
                if matrix[index_row][i] != 0:
                    x = matrix[index_row][index_col + 1]
        # If in result in chosen row all elements equal 0, then no solution.
        if x == 0:
            print("NOT FIND SOLVING ELEMENT")
            return
    else:
        return res
    # Set to place of solving element 1 value, for skip excess operation.
    # Because division with equals elements get in result 1.
    res[index_row][index_col] = 1.0
    i_solve = index_row
    j_solve = index_col
    for i in range(height):
        for j in range(width):
            if i == i_solve:
                # By the G-J method all elements of solving row defined like division on solving element.
                res[i][j] = round((matrix[i][j] / x), 2)
            elif i != i_solve:
                if j == j_solve:
                    # By the G-J method all elements of solving column defined to 0.
                    res[i][j] = 0.0
                else:
                    # Other elements defined by rule of rectangle.
                    res[i][j] = round((((x * matrix[i][j]) - (matrix[i_solve][j] * matrix[i][j_solve])) / x),
                                      fix_point)
            # check_sum += res[i][j]
        # check_sum = 0
    return res


# returns the list of basic solutions
def solve(matrix):
    basic_solution = []
    rec = matrix
    row_count = len(matrix)
    variable_count = len(matrix[0]) - 1
    # Define count of steps to find solution.
    if row_count < variable_count:
        rang = row_count
    else:
        rang = variable_count
    for i in range(rang):
        i_solve = j_solve = i
        rec = JG(rec, i_solve, j_solve)
    for i in range(rang):
        basic_solution.append(rec[i][-1])
    return basic_solution
