from PIL import Image
from src.BaseFile import BaseFile


class ImageFile(BaseFile):
    def __init__(self, file_path):
        super().__init__(file_path)
        try:
            self.__image = Image.open(file_path)
            # define get_color_list() method in advance and stores in private field self.__colors
            # because color list will be apply in other method
            self.__colors = self.get_color_list()
        except IOError as err:
            print(err)

    def get_width(self):
        """
        :return: int - image width
        """
        return self.__image.size[0]

    def get_height(self):
        """
        :return: int - image height
        """
        return self.__image.size[1]

    def get_model_camera(self):
        pass

    def get_iso_value(self):
        pass

    def get_color_list(self):
        """
        :return: list - list of tuples, where first value is color count, second value - tuple - color rgb value
        """
        def sorted_by_decrease(color_list):
            """
            :param color_list: list - list of tuples
            :return: list - list of sorted colors by decrease by count of pixels of color
            """
            length = len(color_list)
            for i in range(1, length):
                # el - the current tuple with color count and rgb value
                el = color_list[i]
                j = i
                # color_list[j - 1][0] - the count of pixels of previous element
                # el[0] - the count of pixels of current element
                while j > 0 and color_list[j - 1][0] < el[0]:
                    color_list[j] = color_list[j - 1]
                    j -= 1
                color_list[j] = el

        self.__colors = self.__image.getcolors(self.get_width() * self.get_height())
        sorted_by_decrease(self.__colors)
        return self.__colors

    def get_most_commonly_color(self):
        """
        :return: list - list of tuple with rgb value
        """
        res = None
        if self.__colors:
            max_color_count = self.__colors[0][0]
            res = [color[1] for color in self.__colors if color[0] == max_color_count]
        return res

    def get_repeatable_files(self):
        pass

i = ImageFile('/home/kate/Pictures/Untitled.png')
print(i.get_permission())
print(i.get_most_commonly_color())
