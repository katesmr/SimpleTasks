def str_list_to_int(list_of_str):
    try:
        return [int(num) for num in list_of_str]
    except ValueError as err:
        print(err)


def split_edit(string, delimeter):
    try:
        return string.split(delimeter)
    except ValueError as err:
        print(err)
