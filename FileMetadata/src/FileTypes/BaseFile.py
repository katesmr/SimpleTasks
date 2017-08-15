from src.core.FileInfo import FileInfo
from src.core.file_type import file_type
from src.core.file_name import file_name
from src.core.file_size import file_size
from src.core.file_owner import file_owner
from src.core.file_permission import file_permission
from src.core.file_modification_date import file_modification_date
from src.core.file_creation_date import file_creation_date


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
        return file_owner(self.file_object)

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
