def image_most_commonly_color(image):
    """
    :param image: Image
    :return: list - list of tuple with rgb value
    """
    result = None
    if image.colors:
        max_color_count = image.colors[0][0]  # in sorted list
        result = [color[1] for color in image.colors if color[0] == max_color_count]
    return result
