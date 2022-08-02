import os
import numpy as np

from linux_tone_keyboard.sound_schemes import sound_schemes
from linux_tone_keyboard.play_sound import PlaySound


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


def load_sound_scheme(sound_scheme_name, pitch_offset=0):
    sounds_dir = "WavTones/"
    d = lambda fp: os.path.join(sounds_dir, fp)
    n = lambda x: Note(note_number=x, filename=d(f"{x}.wav"))

    key_to_sound_dict = get_key_to_sound_dict_raw(sound_scheme_name)

    key_to_sound_dict = {k: (n(v + pitch_offset) if type(v) is int else v) for k,v in key_to_sound_dict.items()}  # so I can just type the MIDI note number

    tone_counts = count_vals(key_to_sound_dict)
    greater_than_one_counts = set([v for v in key_to_sound_dict.values() if tone_counts[v] > 1])
    assert greater_than_one_counts == {None}, f"got multiple-use tones: {sorted(x for x in greater_than_one_counts if x is not None)}"
    return key_to_sound_dict


def play_sound_for_key_code(event_code, key_to_sound_dict, volume):
    if type(event_code) is not str:
        # print(f"event_code is {event_code}, not a string, skipping")
        print("non-str")
    elif event_code.startswith("KEY"):
        # print(event_code)
        # if event_code == "KEY_ENTER":
        #     filename = getcwd() + '/sounds/' + sounds["enter"]
        # elif event_code == "KEY_SPACE":
        #     filename = getcwd() + '/sounds/' + sounds["space"]
        if True:  # else:
            if event_code not in key_to_sound_dict:
                print(f"event code {event_code} not found in key_to_sound_dict")
                # key_sound_pair[event_code] = choice(sounds["click"])
            # filename = getcwd() + '/sounds/' +\
            #     key_sound_pair[event_code]
            else:
                note = key_to_sound_dict[event_code]
                if note is None:
                    # print(f"event code {event_code} was found but has no associated sound")
                    print(f"unassociated: {event_code}")
                else:
                    print(f"Note {note.note_number}_10 = {note.note_number_base_12}_12: {event_code}")
                    PlaySound(note.filename, volume).start()
