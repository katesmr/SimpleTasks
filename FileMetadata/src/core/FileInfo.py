import os


class FileInfo:
    def __init__(self, file_path):
        """
        :param file_path: str - full path to file
        """
        assert type(file_path) is str
        self.file_path = file_path
        try:
            self.stat = os.stat(self.file_path)
            self.file = open(file_path, "rb")
        except (IOError, OSError) as error:
            print(error)

    def __del__(self):
        self.file.close()
