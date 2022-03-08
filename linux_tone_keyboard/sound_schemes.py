# just read the data structures here and store as locals, then other scripts will import this file and have access to them by name

from linux_tone_keyboard.sound_scheme_dicts.original import key_to_sound_dict as original

sound_schemes = {
    "original": original,
}
