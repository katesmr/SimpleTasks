# String operations

String class with simple methods.

# Usage
```
string = MyString("example")
string.set("test for take the most shortest and longest words")
print(string.get_min_max_word())
string.set("00000000000 strip test 00")
print(string.my_strip('0'))
string.set("Pull up if I pull up")
print(string.is_palindrome())
string.set("commonly words used words")
print(string.commonly_used_words())
string.set("""Then this ebony bird beguiling my sad fancy into smiling,
              By the grave and stern decorum of the countenance it wore,
              “Though thy crest be shorn and shaven, thou,” I said, “art sure no craven,
              Ghastly grim and ancient Raven wandering from the Nightly shore—
              Tell me what thy lordly name is on the Night’s Plutonian shore!”
              Quoth the Raven “Nevermore.”""")
print(string.commonly_used_words_with_regex())
```
