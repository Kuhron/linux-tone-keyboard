import os
import numpy as np
sounds_dir = "/home/wesley/WavTones/"
d = lambda fp: os.path.join(sounds_dir, fp)
n = lambda x: Note(note_number=x, filename=d(f"{x}.wav"))


class Note:
    def __init__(self, note_number, filename):
        self.note_number = note_number
        self.filename = filename
        self.note_number_base_12 = convert_to_base_12(self.note_number)


def convert_to_base_12(n, use_note_names=True):
    if use_note_names:
        twelves, ones = divmod(n, 12)
        note_name_char = "CKDHEFXGJARB"[ones]
        return f"{twelves}{note_name_char}"
    else:
        return np.base_repr(n, base=12)


key_to_sound_dict = {
    # sorting it based on my own keyboard
    # first the main section, then the num pad
    # traversed in rows from bottom to top, left to right within row

    "KEY_LEFTCTRL": 30,
    # FN does not make a keypress event by itself
    "KEY_LEFTMETA": 32,
    "KEY_LEFTALT": 34,
    "KEY_SPACE": 35,
    "KEY_RIGHTALT": 33,
    "KEY_RIGHTCTRL": 31,
    "KEY_LEFT": None,
    "KEY_DOWN": None,
    "KEY_RIGHT": None,
    "KEY_UP": None,

    "KEY_LEFTSHIFT": 36,
    "KEY_Z": 40,
    "KEY_X": 44,
    "KEY_C": 48,  # C needs to be a C (multiple of 12 in MIDI number)
    "KEY_V": 52,
    "KEY_B": 56,
    "KEY_N": 60,
    "KEY_M": 64,
    "KEY_COMMA": 68,
    "KEY_DOT": 72,
    "KEY_SLASH": 76,
    "KEY_RIGHTSHIFT": 80,

    "KEY_CAPSLOCK": 37,
    "KEY_A": 41,
    "KEY_S": 45,
    "KEY_D": 49,
    "KEY_F": 53,
    "KEY_G": 57,
    "KEY_H": 61,
    "KEY_J": 65,
    "KEY_K": 69,
    "KEY_L": 73,
    "KEY_SEMICOLON": 77,
    "KEY_APOSTROPHE": 81,
    "KEY_ENTER": 85,

    "KEY_TAB": 38,
    "KEY_Q": 42,
    "KEY_W": 46,
    "KEY_E": 50,
    "KEY_R": 54,
    "KEY_T": 58,
    "KEY_Y": 62,
    "KEY_U": 66,
    "KEY_I": 70,
    "KEY_O": 74,
    "KEY_P": 78,
    "KEY_LEFTBRACE": 82,
    "KEY_RIGHTBRACE": 86,
    "KEY_BACKSLASH": 90,

    "KEY_GRAVE": 39,
    "KEY_1": 43,
    "KEY_2": 47,
    "KEY_3": 51,
    "KEY_4": 55,
    "KEY_5": 59,
    "KEY_6": 63,
    "KEY_7": 67,
    "KEY_8": 71,
    "KEY_9": 75,
    "KEY_0": 79,
    "KEY_MINUS": 83,
    "KEY_EQUAL": 87,
    "KEY_BACKSPACE": 84,

    "KEY_ESC": None,
    "KEY_F1": None,
    "KEY_F2": None,
    "KEY_F3": None,
    "KEY_F4": None,
    "KEY_F5": None,
    "KEY_F6": None,
    "KEY_F7": None,
    "KEY_F8": None,
    "KEY_F9": None,
    "KEY_F10": None,
    "KEY_F11": None,
    "KEY_F12": None,
    "KEY_SYSRQ": None,
    "KEY_INSERT": None,
    "KEY_DELETE": None,

    # treat the FNs as their own row above the top row
    # note that the FN+ESC FNLOCK is also not a keypress event
    "KEY_MUTE": None,
    "KEY_VOLUMEDOWN": None,
    "KEY_VOLUMEUP": None,
    "KEY_PREVIOUSSONG": None,
    "KEY_PLAYPAUSE": None,
    "KEY_NEXTSONG": None,
    # FN+F7 is nothing
    # FN+F8 says it's KEY_P so ignore it
    # FN+F9 has event.code of type int, which crashes the program (TODO fix that with a printed error)
    # FN+F10 is not a keypress
    "KEY_BRIGHTNESSDOWN": None,
    "KEY_BRIGHTNESSUP": None,
    # FN+SYSRQ turns WiFi on/off, has event.code of type int, ignore it
    "KEY_SLEEP": None,  # this is FN+INSERT
    # FN+DELETE is nothing

    # numpad
    "KEY_KP0": None,
    "KEY_KPDOT": None,
    "KEY_KPENTER": None,
    "KEY_KP1": None,
    "KEY_KP2": None,
    "KEY_KP3": None,
    "KEY_KP4": None,
    "KEY_KP5": None,
    "KEY_KP6": None,
    "KEY_KPPLUS": None,
    "KEY_KP7": None,
    "KEY_KP8": None,
    "KEY_KP9": None,
    "KEY_NUMLOCK": None,
    "KEY_KPSLASH": None,
    "KEY_KPASTERISK": None,
    "KEY_KPMINUS": None,
    "KEY_PAGEUP": None,
    "KEY_PAGEDOWN": None,
    "KEY_HOME": None,
    "KEY_END": None,

    # unsorted
    "KEY_RESERVED": None,
    "KEY_SCROLLLOCK": None,
    "KEY_103RD": None,
    "KEY_F13": None,
    "KEY_102ND": None,
    "KEY_F14": None,
    "KEY_F15": None,
    "KEY_F16": None,
    "KEY_F17": None,
    "KEY_F18": None,
    "KEY_F19": None,
    "KEY_F20": None,
    "KEY_LINEFEED": None,
    "KEY_MACRO": None,
    "KEY_POWER": None,
    "KEY_KPEQUAL": None,
    "KEY_KPPLUSMINUS": None,
    "KEY_PAUSE": None,
    "KEY_F21": None,
    "KEY_F22": None,
    "KEY_F23": None,
    "KEY_F24": None,
    "KEY_KPCOMMA": None,
    "KEY_RIGHTMETA": None,  # I don't have this
    "KEY_COMPOSE": None,
    "KEY_STOP": None,
    "KEY_AGAIN": None,
    "KEY_PROPS": None,
    "KEY_UNDO": None,
    "KEY_FRONT": None,
    "KEY_COPY": None,
    "KEY_OPEN": None,
    "KEY_PASTE": None,
    "KEY_FIND": None,
    "KEY_CUT": None,
    "KEY_HELP": None,
    "KEY_MENU": None,
    "KEY_CALC": None,
    "KEY_SETUP": None,
    "KEY_WAKEUP": None,
    "KEY_FILE": None,
    "KEY_SENDFILE": None,
    "KEY_DELETEFILE": None,
    "KEY_XFER": None,
    "KEY_PROG1": None,
    "KEY_PROG2": None,
    "KEY_WWW": None,
    "KEY_MSDOS": None,
    "KEY_COFFEE": None,
    "KEY_DIRECTION": None,
    "KEY_CYCLEWINDOWS": None,
    "KEY_MAIL": None,
    "KEY_BOOKMARKS": None,
    "KEY_COMPUTER": None,
    "KEY_BACK": None,
    "KEY_FORWARD": None,
    "KEY_CLOSECD": None,
    "KEY_EJECTCD": None,
    "KEY_EJECTCLOSECD": None,
    "KEY_STOPCD": None,
    "KEY_RECORD": None,
    "KEY_REWIND": None,
    "KEY_PHONE": None,
    "KEY_ISO": None,
    "KEY_CONFIG": None,
    "KEY_HOMEPAGE": None,
    "KEY_REFRESH": None,
    "KEY_EXIT": None,
    "KEY_MOVE": None,
    "KEY_EDIT": None,
    "KEY_SCROLLUP": None,
    "KEY_SCROLLDOWN": None,
    "KEY_KPLEFTPAREN": None,
    "KEY_KPRIGHTPAREN": None,
    "KEY_INTL1": None,
    "KEY_INTL2": None,
    "KEY_INTL3": None,
    "KEY_INTL4": None,
    "KEY_INTL5": None,
    "KEY_INTL6": None,
    "KEY_INTL7": None,
    "KEY_INTL8": None,
    "KEY_INTL9": None,
    "KEY_LANG1": None,
    "KEY_LANG2": None,
    "KEY_LANG3": None,
    "KEY_LANG4": None,
    "KEY_LANG5": None,
    "KEY_LANG6": None,
    "KEY_LANG7": None,
    "KEY_LANG8": None,
    "KEY_LANG9": None,
    "KEY_PLAYCD": None,
    "KEY_PAUSECD": None,
    "KEY_PROG3": None,
    "KEY_PROG4": None,
    "KEY_SUSPEND": None,
    "KEY_CLOSE": None,
    "KEY_UNKNOWN": None,
}
pitch_offset = 12
key_to_sound_dict = {k: (n(v + pitch_offset) if type(v) is int else v) for k,v in key_to_sound_dict.items()}  # so I can just type the MIDI note number

def count_vals(dct):
    counts = {}
    for v in dct.values():
        if v not in counts:
            counts[v] = 0
        counts[v] += 1
    return counts

tone_counts = count_vals(key_to_sound_dict)
greater_than_one_counts = set([v for v in key_to_sound_dict.values() if tone_counts[v] > 1])
assert greater_than_one_counts == {None}, f"got multiple-use tones: {sorted(x for x in greater_than_one_counts if x is not None)}"
