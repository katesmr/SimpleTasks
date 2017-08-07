def sorted_by_decrease(color_list):
    """
    :param color_list: list - list of tuples
    :return: list - list of sorted colors by decrease by count of pixels of color
    """
    length = len(color_list)
    for i in range(1, length):
        # el - the current tuple with color count and rgb value
        el = color_list[i]
        j = i
        # color_list[j - 1][0] - the count of pixels of previous element
        # el[0] - the count of pixels of current element
        while j > 0 and color_list[j - 1][0] < el[0]:
            color_list[j] = color_list[j - 1]
            j -= 1
        color_list[j] = el
