from tracks import *
import rtmidi
from utilities import init_print
from termcolor import colored, cprint


midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
if available_ports:
    midiout.open_port(1)

DEBUG = init_print(midiout)
t = Track(midiout, debug=DEBUG)

t.main_loop()
