import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from src.core.FileInfo import FileInfo
from src.core.file_type import file_type
from src.core.file_name import file_name
from src.core.file_size import file_size
from src.core.file_owner import file_owner
from src.core.file_permission import file_permission
from src.core.file_modification_date import file_modification_date
from src.core.file_creation_date import file_creation_date
# from src.base.Windows.file_owner_win import file_owner_win


class BaseFile:
    def __init__(self, file_path):
        self.file_object = FileInfo(file_path)

    def get_size(self):
        """
        :return: int - count of bytes of file
        """
        return file_size(self.file_object)

    def get_type(self):
        """
        :return: str - type of media file
        """
        return file_type(self.file_object.file_path)

    def get_owner(self):
        """
        :return: tuple - owner name with user id
        """
        if os.name == "posix":
            result = file_owner(self.file_object)
        else:
            pass
            # result = file_owner_win(self.file_object.file, self.file_object.file_path)
        return result

    def get_name(self):
        """
        :return: str - file name
        """
        return file_name(self.file_object.file_path)

    def get_creation_date(self):
        """
        :return: str - creation data
        """
        return file_creation_date(self.file_object)

    def get_modification_date(self):
        """
        :return: str - modification data
        """
        return file_modification_date(self.file_object)

    def get_permission(self):
        """
        :return: dict - dictionary key is mode, value is permissions of file
        """
        return file_permission(self.file_object)

    def get_description(self):
        """
        :return: str - description text
        """
        pass

    def get_repeatable_files(self):
        """
        :return: list - lit of files with equals content
        """
        pass

f = BaseFile("/home/kate/Documents/пароли.txt")
print(f.get_type())
print(f.get_permission())
print(f.get_creation_date())
print(f.get_modification_date())
print(f.get_size())
print(f.get_owner())
print(f.get_name())
