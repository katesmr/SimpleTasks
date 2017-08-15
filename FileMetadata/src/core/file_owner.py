import os
if os.name == "posix":
    from src.core.Unix.file_author import file_author
else:
    from src.core.Win.file_author import file_author


def file_owner(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: tuple - owner name with user id
    """
    return file_author(file_info)
