import os


def compute_file_size(file):
    old_file_position = file.tell()
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(old_file_position, os.SEEK_SET)
    return size
