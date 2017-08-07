import time


def file_creation_date(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: str - creation data
    """
    return time.asctime(time.localtime(file_info.stat.st_ctime))
