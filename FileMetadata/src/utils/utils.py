def int_dec_to_bin(digit, accuracy=0):
    """
    :param digit: - int
    :param accuracy: - int - count of bit to output
    :return: str - binary number
    """
    def set_format(binary_number, digit_count):
        """
        :param binary_number: - str
        :param digit_count: - int - count of bit to output
        :return: str - binary number with fixed count of bits
        """
        formatted_number = ""
        length = len(binary_number)
        remainder = digit_count - length
        if remainder:
            #  adding missing bits
            for i in range(remainder):
                formatted_number += '0'
            formatted_number += binary_number[:]
        else:
            # cutting excess bits
            remainder *= -1
            formatted_number = binary_number[remainder:]
        return formatted_number

    assert type(digit) is int
    assert type(accuracy) is int
    # convert dec to bin
    res = "{0:b}".format(digit)
    if accuracy:
        if accuracy != len(res):
            res = set_format(res, accuracy)
    return res


def split_on_bit(permission_number, bits_count=1):
    """
    :param permission_number: str - permission number
    :param bits_count: int - count of bit for the output
    :return: list - list, where number represented like bits
    """
    result = []
    number = list(permission_number)
    for num in number:
        # each integer number represent like binary number
        tmp = int_dec_to_bin(int(num), bits_count)
        result.append(list(tmp))
    return result


def permission(bit_list):
    """
    Convert permission numbers to string
    :param bit_list: - list of bits
    :return: dict - dictionary key is mode, value is permissions of file
    """
    res = {}
    mode_list = ("user", "group", "other")
    permission_list = ("read", "write", "execute")
    tmp = []
    for index, token in enumerate(mode_list):
        for bit_index, bit in enumerate(bit_list[index]):
            # permission exist only if bit equal 1
            # on this bit index defined corresponding permission title
            if bit == '1':
                tmp.append(permission_list[bit_index])
        res[token] = tmp
        tmp = []
    return res
