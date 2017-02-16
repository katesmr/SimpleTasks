import re


def get_all_most_word(string):
    splitted_string = string.lower().split()
    words_dict = {}
    for word in splitted_string:
        if word.isalnum():
            # check for the presence of current word in the key
            if word in words_dict:
                words_dict[word] += 1  # increase words counter
            else:
                words_dict[word] = 1  # create new value because it is new word
    max_value = max(words_dict.values())
    return [key for key in words_dict.keys() if words_dict[key] == max_value]


def get_all_most_word_with_regex(string):
    string = string.lower()
    splitted_string = re.findall(r"\b[a-zA-Z-]+\b", string)
    words_dict = {}
    for word in splitted_string:
        # check for the presence of current word in the key
        if word in words_dict:
            words_dict[word] += 1  # increase words counter
        else:
            words_dict[word] = 1  # create new value because it is new word
    max_value = max(words_dict.values())
    return [key for key in words_dict.keys() if words_dict[key] == max_value]
