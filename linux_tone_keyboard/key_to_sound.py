import os
import numpy as np
from linux_tone_keyboard.sound_schemes import sound_schemes

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


def count_vals(dct):
    counts = {}
    for v in dct.values():
        if v not in counts:
            counts[v] = 0
        counts[v] += 1
    return counts


def get_key_to_sound_dict_raw(sound_scheme_name):
    return sound_schemes[sound_scheme_name]


def load_sound_scheme(sound_scheme_name):
    sounds_dir = "/home/wesley/WavTones/"
    d = lambda fp: os.path.join(sounds_dir, fp)
    n = lambda x: Note(note_number=x, filename=d(f"{x}.wav"))

    key_to_sound_dict = get_key_to_sound_dict_raw(sound_scheme_name)

    pitch_offset = 12
    key_to_sound_dict = {k: (n(v + pitch_offset) if type(v) is int else v) for k,v in key_to_sound_dict.items()}  # so I can just type the MIDI note number

    tone_counts = count_vals(key_to_sound_dict)
    greater_than_one_counts = set([v for v in key_to_sound_dict.values() if tone_counts[v] > 1])
    assert greater_than_one_counts == {None}, f"got multiple-use tones: {sorted(x for x in greater_than_one_counts if x is not None)}"
    return key_to_sound_dict
