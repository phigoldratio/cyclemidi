
OP = ["+", "-", "#", "~", "&", "~#", ]
ACTIONS = {"cycle": {"inputs": ["id", "cycle"], "parameters": ["speed", "reboot"]},
           "launch" : {"inputs"  : ["id", "num"], 'parameters' : ["loop", "next_bar"]},
           "stop" : {"inputs"  : ["id", "num"], 'parameters' : ["next_bar"]},
           "mod" : {"inputs"  : ["id", "cycle"], 'parameters' : ["speed", "loop", "reboot", "next_bar"]},
           "exit" : {"inputs" : [], "parameters" : []},
           "mv" : {"inputs" : ["id","num","num"], "parameters" : []},
           "help" : {"inputs" : ["id"]}}
NOTES = ['a', 'bb', "b", "c", "db", "d", "eb", "e", "f", "gb", "g", "ab"]
TEMPO = 1
SUBD = 16
GLOBAL_CYCLE = 8

def is_note(s: str):
    if len(s) == 2:
        return s[0] in "abcdefg" and s[1].isnumeric()
    elif len(s) == 3:
        return s[0] in "abcdefg" and s[1] == "b" and s[2].isnumeric()
    else:
        return False
