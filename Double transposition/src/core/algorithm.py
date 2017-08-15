def create_matrix_message(size, message):
    """
    :param size: int - size of matrix
    :param message: str
    :return: list - list of str
    """
    tmp = ""
    index = 0
    matrix = ["" for _ in range(size)]
    if len(message) < size * size:
        for i in range(size):
            # Adding spaces to end of message for message length equals (size*size)
            message += " "
    # Full list of splitted message by size
    for i in range(size):
        for j in range(size):
            tmp += message[index]
            index += 1
        matrix[i] = tmp
        tmp = ""
    return matrix


def decode(matrix, column_key, row_key):
    """
    :param matrix: list - source message for decoding represented like list of str
    :param column_key: list - list of numbers by which will sort columns of matrix
    :param row_key: list - list of numbers by which will sort row of matrix
    :return: tuple - sorted rows, sorted columns, decoded message
    """
    res = ""
    tmp = ""
    row_sorted = []
    column_sorted = []
    size = len(matrix)
    # Sorting rows by key numbers consider order in row_key list
    for i in range(size):
        row_sorted.append(matrix[row_key[i] - 1])
    # Sorting columns by key numbers consider order in column_key list
    for i in range(size):
        for j in range(size):
            tmp += row_sorted[i][column_key[j] - 1]
        column_sorted.append(tmp)
        res += tmp  # save decoding message in string
        tmp = ""
    return row_sorted, column_sorted, res


def code(matrix, column_key, row_key):
    """
    :param matrix: list - source message for coding represented like list of str
    :param column_key: list - list of numbers by which will sort columns of matrix
    :param row_key: list - list of numbers by which will sort row of matrix
    :return: tuple - sorted columns, sorted rows, coded message
    """
    res = ""
    tmp = ""
    row_sort = []
    column_sort = []
    size = len(matrix)
    # Sorting columns by index key in column_key
    for i in range(size):
        for j in range(size):
            tmp += matrix[i][column_key.index(j+1)]
        column_sort.append(tmp)
        tmp = ""
    # Sorting rows by index key in row_key
    for i in range(size):
        row = column_sort[row_key.index(i+1)]
        row_sort.append(row)
        res += row  # save coding message in string
    return column_sort, row_sort, res
