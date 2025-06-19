import time
from colorama import Fore, Style

from termcolor import colored

LOGO = colored(""" ██████╗██╗   ██╗ ██████╗██╗     ███████╗        ███╗   ███╗██╗██████╗ ██╗
██╔════╝╚██╗ ██╔╝██╔════╝██║     ██╔════╝        ████╗ ████║██║██╔══██╗██║
██║      ╚████╔╝ ██║     ██║     █████╗          ██╔████╔██║██║██║  ██║██║
██║       ╚██╔╝  ██║     ██║     ██╔══╝          ██║╚██╔╝██║██║██║  ██║██║
╚██████╗   ██║   ╚██████╗███████╗███████╗        ██║ ╚═╝ ██║██║██████╔╝██║
 ╚═════╝   ╚═╝    ╚═════╝╚══════╝╚══════╝        ╚═╝     ╚═╝╚═╝╚═════╝ ╚═╝
""", 'white', attrs=['reverse'])
AUTHOR = colored("PhiGoldRatio", "blue")
ENTER = colored("ENTER","blue", attrs=["blink"])
VERSION = "v.O.7.1"

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

def init_print(midiout):
    print(LOGO)
    print(f"Cyclemidi {VERSION} by", AUTHOR,"\nConfigure Midi output then press ", ENTER,
          "\nFor help, press 'help : all' for general help and basic tutorial")
    temp = input()
    debug = False
    if temp == "d":
        debug = True
        print(colored("ENTERING DEBUG MODE", "red", attrs=["blink"]))
        midiout.send_message([0x90, 60, 112])
        time.sleep(0.5)
        midiout.send_message([0x80, 60, 0])
        midiout.send_message([0x90, 63, 112])
        time.sleep(0.5)
        midiout.send_message([0x80, 63, 0])
        midiout.send_message([0x90, 67, 112])
        time.sleep(0.5)
        midiout.send_message([0x80, 67, 0])
    else:
        midiout.send_message([0x90, 60, 112])
        time.sleep(0.5)
        midiout.send_message([0x80, 60, 0])
        midiout.send_message([0x90, 64, 112])
        time.sleep(0.5)
        midiout.send_message([0x80, 64, 0])
        midiout.send_message([0x90, 67, 112])
        time.sleep(0.5)
        midiout.send_message([0x80, 67, 0])

    return debug




