import os
import time
from os.path import basename
import magic
from utils.utils import split_on_bit, permission


class BaseFile:
    def __init__(self, file_path):
        """
        :param file_path: str - full path to file
        """
        assert type(file_path) is str
        self.__file_stat = None
        self.__file_path = file_path
        try:
            # create stat object
            self.__file_stat = os.stat(self.__file_path)
        except (IOError, FileExistsError) as err:
            print(err)

    def get_size(self):
        """
        :return: int - count of bytes of file
        """
        return self.__file_stat.st_size

    def get_type(self):
        """
        :return: str - type of media file
        """
        # definition instances of Magic class, which provide access to libmagics‘s file identification capabilities
        # MAGIC_MIME_TYPE - definition mime type
        magic_object = magic.Magic(flags=magic.MAGIC_MIME_TYPE)
        # id_filename - identify a file from filename.
        file_type = magic_object.id_filename(self.__file_path)
        return file_type

    def get_owner(self):
        """
        :return: tuple - owner name with user id
        """
        try:
            import pwd  # UNIX platform
        except ImportError:
            import winpwd as pwd  # Windows
        finally:
            result = pwd.getpwuid(self.__file_stat.st_uid)
            return result[0], result[2]

    def get_name(self):
        """
        :return: str - file name
        """
        return basename(self.__file_path)

    def get_creation_date(self):
        """
        :return: str - creation data
        """
        return time.asctime(time.localtime(self.__file_stat.st_ctime))

    def get_modification_date(self):
        """
        :return: str - modification data
        """
        return time.asctime(time.localtime(self.__file_stat.st_mtime))

    def __get_permission_number(self):
        """
        :return: str - permission number in octal numeral system
        """
        return oct(self.__file_stat.st_mode)[-3:]

    def get_permission(self):
        """
        :return: dict - dictionary key is mode, value is permissions of file
        """
        file_permission = self.__get_permission_number()
        split_permission = split_on_bit(file_permission, 3)
        result = permission(split_permission)
        return result

    def get_description(self):
        pass

    def get_repeatable_files(self):
        """
        :return: list - lit of files with equals content
        """
        pass
