# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 2 -*-
# Author: Fábio André Damas <skkeeper at gmail dot com>

from os import listdir, getcwd
from random import choice
from third_party.evdev import DeviceGroup
from linux_tone_keyboard.play_sound import PlaySound
from linux_tone_keyboard.detect_keyboards import detect_keyboards
from linux_tone_keyboard.key_to_sound import load_sound_scheme
from optparse import OptionParser
from signal import signal, SIGINT
from sys import exit


# Handle CTRL+C
def signal_handler(signal, frame):
    print('\033[1;32mCTRL + C Detected. Exiting ...')
    print('Ignore any errors after this message.\033[1;m')
    exit(0)
signal(SIGINT, signal_handler)

# Handle arguments
parser = OptionParser()
parser.add_option(
    '-v', '--volume', action="store", dest='volume',
    help="sets the volume of the clicks, anything above 1 will increase the " +
    "volume, and anything less will decrease it. Don't use numbers bigger " +
    "than 2")

parser.set_defaults(volume=1)
(options, args) = parser.parse_args()

# Get a list of sound files
sounds = listdir(getcwd() + '/sounds')
sound_tmp = {}
sound_tmp["click"] = []
for sound in sounds:
    if sound == 'enter.wav':
        sound_tmp["enter"] = sound
    elif sound == 'space.wav':
        sound_tmp["space"] = sound
    else:
        sound_tmp["click"].append(sound)
sounds = sound_tmp
# Volume: Negative to lower the volume
volume = str(options.volume)

# key_sound_pair = dict()
key_to_sound_dict = load_sound_scheme("original")
dev = DeviceGroup(detect_keyboards())
while 1:
    event = dev.next_event()
    if event is not None:
        # print(repr(event))
        if event.type == "EV_KEY" and event.value == 1:
            if type(event.code) is not str:
                # print(f"event.code is {event.code}, not a string, skipping")
                print("non-str")
            elif event.code.startswith("KEY"):
                # print(event.code)
                # if event.code == "KEY_ENTER":
                #     filename = getcwd() + '/sounds/' + sounds["enter"]
                # elif event.code == "KEY_SPACE":
                #     filename = getcwd() + '/sounds/' + sounds["space"]
                if True:  # else:
                    if event.code not in key_to_sound_dict:
                        print(f"event code {event.code} not found in key_to_sound_dict")
                        # key_sound_pair[event.code] = choice(sounds["click"])
                    # filename = getcwd() + '/sounds/' +\
                    #     key_sound_pair[event.code]
                    else:
                        note = key_to_sound_dict[event.code]
                        if note is None:
                            # print(f"event code {event.code} was found but has no associated sound")
                            print("unassociated")
                        else:
                            print(f"Note {note.note_number}_10 = {note.note_number_base_12}_12")
                            PlaySound(note.filename, volume).start()
