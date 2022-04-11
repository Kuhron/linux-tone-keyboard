import sys
import time

from linux_tone_keyboard.char_to_key import char_to_key_dict
from linux_tone_keyboard.key_to_sound import load_sound_scheme, play_sound_for_key_code


try:
    fp = sys.argv[1]
except IndexError:
    print("No file specified! You must specify a file as an argument to the program.")
    sys.exit()

print(f"playing string in file {fp}")
sound_scheme = "original_no_functions"
key_to_sound_dict = load_sound_scheme(sound_scheme)
print(f"using sound scheme {sound_scheme}")
volume = 1

with open(fp) as f:
    contents = f.read()

for char in contents:
    key_code = char_to_key_dict.get(char)
    if key_code is not None:
        play_sound_for_key_code(key_code, key_to_sound_dict, volume)
        time.sleep(0.1)
