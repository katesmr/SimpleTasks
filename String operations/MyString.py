import re


class MyString(str):
    def __init__(self, string):
        super().__init__()
        self.__string = string

    def set(self, new_string):
        self.__string = new_string

    def get(self):
        return self.__string

    def get_min_max_word(self):
        """
        :return: list with list of shortest words and list of longest words
        """
        def words_set(conditional_value):
            return [words[i] for i in range(length) if words_len_list[i] == conditional_value]

        res = None
        if len(self.__string):
            words = re.findall(r'\b[a-zA-Z-]+\b', self.__string)
            words_len_list = list(map(len, words))
            length = len(words_len_list)
            shortest_length = min(words_len_list)
            longest_length = max(words_len_list)
            shortest_words = words_set(shortest_length)
            longest_words = words_set(longest_length)
            res = [shortest_words, longest_words]
        return res

    def my_strip(self, pattern):
        """
        @see python string strip() method
        """
        res = None
        length = len(self.__string)
        if length:
            res = self.__string[:]
            for char in res:
                if char == pattern:
                    res = res[1:]
                else:
                    break
            length_cutting_string = len(res)
            i = length_cutting_string - 1
            while res[i] == pattern:
                res = res[:-1]
                i -= 1
        return res

    def is_palindrome(self):
        res = None
        if len(self.__string):
            if ' ' in self.__string:
                norm_string = "".join((self.__string[:].lower()).split())
                reversed_string = "".join((self.__string[::-1].lower()).split())
            else:
                norm_string = self.__string
                reversed_string = self.__string[::-1]
            res = norm_string == reversed_string
        return res

    def commonly_used_words(self):
        """
        :return: list of commonly used words in text, otherwise returns list of words of text
        """
        res = None
        if len(self.__string):
            splitting_string = self.__string.lower().split()
            words_dict = {}
            for word in splitting_string:
                if word.isalnum():
                    # check for the presence of current word in the key
                    if word in words_dict:
                        words_dict[word] += 1  # increase words counter
                    else:
                        words_dict[word] = 1  # create new value because it is new word
            max_value = max(words_dict.values())
            res = [key for key in words_dict.keys() if words_dict[key] == max_value]
        return res

    def commonly_used_words_with_regex(self):
        """
        :return: list of commonly used words in text, otherwise returns list of words of text
        """
        res = None
        if len(self.__string):
            string = self.__string.lower()
            splitting_string = re.findall(r"\b[a-zA-Z-]+\b", string)
            words_dict = {}
            for word in splitting_string:
                # check for the presence of current word in the key
                if word in words_dict:
                    words_dict[word] += 1  # increase words counter
                else:
                    words_dict[word] = 1  # create new value because it is new word
            max_value = max(words_dict.values())
            res = [key for key in words_dict.keys() if words_dict[key] == max_value]
        return res
