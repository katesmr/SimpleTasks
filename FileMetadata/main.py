import os
import sys
"""
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
"""
from src.FileTypes.BaseFile import BaseFile
from src.FileTypes.ImageFile import ImageFile
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../"))


if __name__ == "__main__":
    f = BaseFile("/home/kate/Documents/пароли.txt")
    print(f.get_type())
    print(f.get_permission())
    print(f.get_creation_date())
    print(f.get_modification_date())
    print(f.get_size())
    print(f.get_owner())
    print(f.get_name())

    i = ImageFile('/home/kate/Pictures/Untitled.png')
    print(i.get_permission())
    print(i.get_most_commonly_color())
    print(i.get_description())
    print(i.get_comment())
    print(i.get_color_list())
    print(i.get_repeatable_files("/home/kate/Pictures/"))
