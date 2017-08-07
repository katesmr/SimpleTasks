import pwd


def file_owner(file_info):
    """
    :param file_info: FileInfo - FileInfo object
    :return: tuple - owner name with user id
    """
    owner_id = file_info.stat.st_uid
    owner_name = pwd.getpwuid(owner_id)[0]
    return owner_name, owner_id
