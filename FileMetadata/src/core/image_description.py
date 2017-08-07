def image_description(image):
    """
    :param image: Image
    :return: str - description text
    """
    result = {}
    if "description" in image.info:
        result["description"] = image.info["description"]
    if "Comment" in image.info:
        result["Comment"] = image.info["Comment"]
    return result
