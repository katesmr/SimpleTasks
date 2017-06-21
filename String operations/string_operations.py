import re


# returns list with list of shortest words and list of longest words
def get_min_max_word(string):
    def words_set(conditional_value):
        return [words[i] for i in range(length) if words_len_list[i] == conditional_value]

    words = re.findall(r'\b[a-zA-Z-]+\b', string)
    words_len_list = list(map(len, words))
    length = len(words_len_list)
    shortest_length = min(words_len_list)
    longest_length = max(words_len_list)
    shortest_words = words_set(shortest_length)
    longest_words = words_set(longest_length)
    return [shortest_words, longest_words]


# see python string strip() method
def my_strip(string, pattern):
    for char in string:
        if char == pattern:
            string = string[1:]
        else:
            break
    length = len(string)
    i = length - 1
    while string[i] == pattern:
        string = string[:-1]
        i -= 1
    return string


def is_palindrome(string):
    if ' ' in string:
        norm_string = "".join((string[:].lower()).split())
        reversed_string = "".join((string[::-1].lower()).split())
    else:
        norm_string = string
        reversed_string = string[::-1]
    return norm_string == reversed_string


# returns list of commonly used words in text, otherwise returns list of words of text
def commonly_used_words(string):
    splitting_string = string.lower().split()
    words_dict = {}
    for word in splitting_string:
        if word.isalnum():
            # check for the presence of current word in the key
            if word in words_dict:
                words_dict[word] += 1  # increase words counter
            else:
                words_dict[word] = 1  # create new value because it is new word
    max_value = max(words_dict.values())
    return [key for key in words_dict.keys() if words_dict[key] == max_value]


def commonly_used_words_with_regex(string):
    string = string.lower()
    splitting_string = re.findall(r"\b[a-zA-Z-]+\b", string)
    words_dict = {}
    for word in splitting_string:
        # check for the presence of current word in the key
        if word in words_dict:
            words_dict[word] += 1  # increase words counter
        else:
            words_dict[word] = 1  # create new value because it is new word
    max_value = max(words_dict.values())
    return [key for key in words_dict.keys() if words_dict[key] == max_value]
