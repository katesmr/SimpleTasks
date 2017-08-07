from src.core.base.sorted_by_decrease import sorted_by_decrease


def image_color_list(image, width, height):
    """
    :param image: ImageFile
    :return: list - list of tuples, where first value is color count, second value - tuple - color rgb value
    """

    colors = image.getcolors(width * height)
    sorted_by_decrease(colors)
    return colors
