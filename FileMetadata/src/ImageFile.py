from PIL import Image
from src.BaseFile import BaseFile


class ImageFile(BaseFile):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.__image = Image.open(file_path)

    def get_model_camera(self):
        pass

    def get_iso_value(self):
        pass

    def get_color_list(self):
        pass

    def get_most_commonly_color(self):
        pass

    def get_repeatable_files(self):
        pass
