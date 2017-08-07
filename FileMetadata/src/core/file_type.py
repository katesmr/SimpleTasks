import magic


def file_type(file_path):
    """
    :param file_path: str
    :return: str - type of media file
    """
    assert type(file_path) is str
    # definition instances of Magic class, which provide access to libmagics‘s file identification capabilities
    # MAGIC_MIME_TYPE - definition mime type
    magic_object = magic.Magic(flags=magic.MAGIC_MIME_TYPE)
    # id_filename - identify a file from filename.
    result = magic_object.id_filename(file_path)
    return result
