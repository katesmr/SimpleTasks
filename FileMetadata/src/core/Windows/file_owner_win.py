import win32api
import win32con
import win32security


def file_owner_win(file, file_path):
    """
    :param file:
    :param file_path: str
    :return: tuple - owner name with user id
    """
    # open(FILENAME, "w").close()
    assert type(file_path) is str
    sd = win32security.GetFileSecurity(file_path, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sd.GetSecurityDescriptorOwner()
    owner_name = win32security.LookupAccountSid(None, owner_sid)[0]
    user_id = win32api.GetUserName()
    return owner_name, user_id
