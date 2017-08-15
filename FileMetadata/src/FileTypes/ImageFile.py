from PIL import Image

from src.FileTypes.BaseFile import BaseFile
from src.core.image_color_list import image_color_list
from src.core.image_comment import image_comment
from src.core.image_description import image_description
from src.core.image_exif_data import image_exif_data
from src.core.image_most_commonly_color import image_most_commonly_color
from src.core.repeatable_images_searcher import find_repeatable_images


class ImageFile(BaseFile):
    def __init__(self, file_path):
        super().__init__(file_path)
        try:
            self.image = Image.open(file_path)
            # define get_color_list() method in advance and stores in private field self.__colors
            # because color list will be apply in other method
            self.width = self.image.size[0]
            self.height = self.image.size[1]
            self.colors = self.get_color_list()
        except IOError as err:
            print(err)

    def get_width(self):
        """
        :return: int - image width
        """
        return self.width

    def get_height(self):
        """
        :return: int - image height
        """
        return self.height

    def get_exif_data(self):
        """
        :return: dict
        """
        return image_exif_data(self.image)

    def get_color_list(self):
        """
        :return: list - list of tuples, where first value is color count, second value - tuple - color rgb value
        """
        return image_color_list(self.image, self.width, self.height)

    def get_most_commonly_color(self):
        """
        :return: list - list of tuple with rgb value
        """
        return image_most_commonly_color(self)

    def get_repeatable_files(self, path):
        """
        :return:
        """
        return find_repeatable_images(path, self.image)

    def get_description(self):
        """
        :return: str - description text
        """
        return image_description(self.image)

    def get_comment(self):
        """
        :return: str - description text
        """
        return image_comment(self.image)
