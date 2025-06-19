import threading
import time
from rich.console import Console
from rich.markdown import Markdown
from termcolor import colored
from interpreter import *
from midi_sending import send_midi, midi_off
from help import *

command_input = ""
current_command_input = ""


def fn_input():
    global command_input
    print(colored(">", "blue", attrs=["blink"]), end="  ")
    command_input = input()


class Track:
    def __init__(self, midiout, debug=False):
        self.midiout = midiout
        self.stored = dict()
        self.launched = {x: [] for x in range(11)}
        self.temp = {x: [] for x in range(11)}
        self.values = None
        self.clock = 0
        self.debug = debug

    def get_output(self):
        self.values = list()
        for k, cycles in self.launched.items():
            for cycle in cycles:
                self.values.append((k, list(cycle.values())[0].get_out()))

    def update_cycles(self):
        for cycles in self.launched.values():
            for cycle in cycles:
                list(cycle.values())[0].update_time()

    def main_loop(self):
        global command_input
        global current_command_input

        thread_input = threading.Thread(target=fn_input)
        thread_input.start()
        midi_sent = []
        while True:
            if self.clock % (SUBD * GLOBAL_CYCLE) == 0:

                if self.debug:
                    print(f"new bar : stored = {self.stored} ; launched = {self.launched}")

                self.clock = 0
                for k, v in self.temp.items():
                    for c in v:
                        self.launched[k].append(c)
                self.temp = {x: [] for x in range(11)}
            if command_input != current_command_input:
                try :
                    self.get_command(command_input)
                except ValueError as err:
                    print(colored(f"{err} \n synthax error, please retry", "red"))
                current_command_input = command_input
                thread_input = threading.Thread(target=fn_input)
                thread_input.start()

            self.get_output()

            midi_sent = []
            for val in self.values:
                if val is not None:
                    if val[1] is not None:
                        val = self.compute(val)
                        if val[1] is not None:

                            if val[1].typ == "chord":
                                for v in val[1].value.notes:
                                    if v is not None:
                                        midi_sent.append((val[0], v))
                            else:
                                if val is not None:
                                    midi_sent.append(val)
            self.clock += 1
            for note in midi_sent:
                send_midi(channel=note[0],value=note[1], midiout=self.midiout, debug=self.debug)

            time.sleep(TEMPO / SUBD)

            for note in midi_sent:
                midi_off(note, self.midiout)

            self.update_cycles()

    def compute(self, val):
        if val[1] is not None:
            if val[1].typ == "ref":
                val = (val[0], val[1].value.get_ref(self.launched))
                # print(f"ref with val : {val}")
                return self.compute(val)
            elif val[1].typ == "chord":
                # print(val)
                return val[0], val[1].copy_with(val=[self.compute((val[0], v))[1] for v in val[1].value.notes],
                                                typ="chord")
            elif val[1].typ == "operation":
                temp_l = self.compute((val[0], val[1].value.left_parameter))[1]
                temp_r = self.compute((val[0], val[1].value.right_parameter))[1]

                temp = (val[0], val[1].value.evaluate(l=temp_l, r=temp_r))
                # print(f"op  {temp}")
                # print(f"result : {val}")
                return self.compute(temp)
            else:
                # print(val)
                return val

        else:
            return val

    def get_action(self, action: Action):

        if action is None:
            pass
        elif action.action == "cycle":
            val = action.inputs[1].value
            if not action.parameters.get('speed') is None:
                val.speed = int(action.parameters.get('speed'))
            if not action.parameters.get('reboot') is None:
                val.reboot = action.parameters.get('reboot') in ("1", "X", "true", "True", "yes", "y")
            self.stored[action.inputs[0].value] = val
            print(f"cycle '{action.inputs[0].value}' added with values :  {val}")

        elif action.action == "launch":
            val = self.stored[action.inputs[0].value]
            track = action.inputs[1].value
            dic = dict()
            dic[action.inputs[0].value] = val
            self.temp[track].append(dic)
            print(f"cycle {action.inputs[0].value} added on chanel {track}")


        elif action.action == "stop":
            index = None
            for i, cycle in enumerate(self.launched[action.inputs[1].value]):
                if list(cycle.keys())[0] == action.inputs[0].value:
                    index = i
            if index is None:
                raise ValueError(f"cycle {action.inputs[0]} not found")
            else:
                del self.launched[action.inputs[1].value][index]
                print(f"cycle '{action.inputs[0].value}' removed on chanel {action.inputs[1].value}")

        elif action.action == "mod":
            # print(self.stored)
            val = action.inputs[1].value
            if not action.parameters.get('speed') is None:
                val.speed = int(action.parameters.get('speed'))
            if not action.parameters.get('reboot') is None:
                val.reboot = action.parameters.get('reboot') in ("1", "X", "true", "True", "yes", "y")
            for k in self.stored.keys():
                if k == action.inputs[0].value:
                    self.stored[k] = val
            for k, v in self.launched.items():
                for i in range(len(v)):
                    if list(v[i].keys())[0] == action.inputs[0].value:
                        self.launched[k][i] = {action.inputs[0].value: val}
            print(f"cycle '{action.inputs[0].value}' changed to {val}")

        elif action.action == "mv":
            for i, v in enumerate(self.launched[action.inputs[1].value]):
                if list(v.keys())[0] == action.inputs[0].value:
                    self.launched[action.inputs[2].value].append(v)
                    del self.launched[action.inputs[1].value][i]
            print(f"cycle '{action.inputs[0].value}' moved from {action.inputs[1].value} to {action.inputs[2].value}")

        elif action.action == "help":
            if not action.parameters.get("command") is None:
                console = Console()
                markdown = Markdown(HELP_MESSAGE_EN[action.parameters.get("command")])
            else:
                console = Console()
                markdown = Markdown(GENERAL_HELP_MESSAGE_FR)
                console.print(markdown)

        elif action.action == "exit":
            del self.midiout
            exit()

    def get_command(self, command: str):
        self.get_action(interpret_input(command))
