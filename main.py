# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 2 -*-
# Author: Fábio André Damas <skkeeper at gmail dot com>

from os import listdir, getcwd
from random import choice
from third_party.evdev import DeviceGroup
from linux_tone_keyboard.detect_keyboards import detect_keyboards
from linux_tone_keyboard.key_to_sound import load_sound_scheme, play_sound_for_key_code
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

# # Get a list of sound files
# sounds = listdir(getcwd() + '/sounds')
# sound_tmp = {}
# sound_tmp["click"] = []
# for sound in sounds:
#     if sound == 'enter.wav':
#         sound_tmp["enter"] = sound
#     elif sound == 'space.wav':
#         sound_tmp["space"] = sound
#     else:
#         sound_tmp["click"].append(sound)
# sounds = sound_tmp

# Volume: Negative to lower the volume
volume = str(options.volume)

sound_scheme = "original_no_functions"
pitch_offset = 3
key_to_sound_dict = load_sound_scheme(sound_scheme, pitch_offset)
dev = DeviceGroup(detect_keyboards())

while True:
    event = dev.next_event()
    if event is not None:
        # print(repr(event))
        if event.type == "EV_KEY" and event.value == 1:
            play_sound_for_key_code(event.code, key_to_sound_dict, volume)

