

from data import *
from data_types import *

class Action:
    def __init__(self, action, inputs, parameters):
        self.action = action
        self.inputs = inputs
        self.parameters = parameters

    def __repr__(self):

        return f"ACTION : {self.action}   INPUTS : {self.inputs}   with PARAMETERS : {self.parameters}"

def interpret_input(inpt : str):
    inpt = inpt.strip()
    inpt = inpt.strip(">")
    inpt = inpt.strip()

    if inpt == "exit":
        return Action("exit", None, None)
    if inpt == "":
        return None
    required = inpt.split("|")
    action = required[0].split(":")[0].strip()
    if not action in ACTIONS.keys():
        raise ValueError(f"action {action} do not exist")

    inputs = [Data(x.strip()) for x in required[0].split(":")[1].split(";") if x != ""]
    if len(inputs) != len(ACTIONS[action]["inputs"]):
        raise ValueError(f"number of parameters incorrect, {len(inputs)}/{len(ACTIONS[action]["inputs"])}")

    parameters = dict()
    if len(required) == 2 :
        par = required[1].split(";")
        parameters = dict()
        for p in par:
            [a,b] = p.split(":")
            a, b = a.strip(), b.strip()
            if a not in ACTIONS[action]["parameters"]:
                raise ValueError(f"parameter '{a}' do not exist")
            parameters[a] = b

    value = Action(action, inputs, parameters)

    return value

