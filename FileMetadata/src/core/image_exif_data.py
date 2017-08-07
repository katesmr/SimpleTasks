from PIL.ExifTags import TAGS


def image_exif_data(image):
    """
    :param image: Image
    :return: dict
    """
    result = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            result[decoded] = value
    return result
