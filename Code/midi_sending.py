from data_types import Note, Data
from data import *


def send_midi(channel, value, midiout, debug=False):
    if debug:
        print(f"{value} sne ton channel {channel}")
    if channel != 0:
        if isinstance(value, Note):
            midiout.send_message([0x90 + channel - 1, value.value, 127])
        if isinstance(value, Data):
            if value.typ == "num":
                midiout.send_message([0x90 + channel - 1, value.value, 127])
            if value.typ == "note":
                midiout.send_message([0x90 + channel - 1, value.value.value, 127])

    # print(f"{value}", end=" ")


def midi_off(note, midiout):
    channel, value = note
    if channel != 0 :
        if isinstance(value, Note):
            midiout.send_message([0x80 + channel - 1, value.value, 0])
        if isinstance(value, Data):
            if value.typ == "num":
                midiout.send_message([0x80 + channel - 1, value.value, 0])
            if value.typ == "note":
                midiout.send_message([0x80 + channel - 1, value.value.value, 0])
