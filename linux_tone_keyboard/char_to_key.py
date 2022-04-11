# for playing the key sounds for words

import string


char_to_key_dict = {}

for x in string.ascii_uppercase:
    char_to_key_dict[x] = f"KEY_{x}"

for x in string.ascii_lowercase:
    char_to_key_dict[x] = f"KEY_{x.upper()}"

for x in "0123456789":
    char_to_key_dict[x] = f"KEY_{x}"

# special ones
char_to_key_dict.update({
    " ": "KEY_SPACE",
    ",": "KEY_COMMA",
    ".": "KEY_DOT",
    "/": "KEY_SLASH",
    "?": "KEY_SLASH",  # maybe later can do something to indicate the different "cases" of these punctuation keys, maybe play a caps-lock tone before them or something
    ";": "KEY_SEMICOLON",
    ":": "KEY_SEMICOLON",
    "'": "KEY_APOSTROPHE",
    "\"": "KEY_APOSTROPHE",
    "`": "KEY_GRAVE",
    "-": "KEY_MINUS",
    "_": "KEY_MINUS",
    "=": "KEY_EQUAL",
    "+": "KEY_EQUAL",
})


if __name__ == "__main__":
    print("char_to_key_dict is:")
    print(char_to_key_dict)
