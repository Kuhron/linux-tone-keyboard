# just read the data structures here and store as locals, then other scripts will import this file and have access to them by name

from linux_tone_keyboard.sound_scheme_dicts.original import key_to_sound_dict as original
from linux_tone_keyboard.sound_scheme_dicts.original_no_functions import key_to_sound_dict as original_no_functions


sound_schemes = {
    "original": original,
    "original_no_functions": original_no_functions,
}
