
from cycles import Cycle
from data import *
from references import Reference
from operations import Operation
from chords import Chord


class Data:

    def __init__(self, raw_data, from_op=False):
        self.raw_data =raw_data
        self.typ = None
        self.value = None
        if not raw_data is None:
            if from_op:
                if isinstance(self.raw_data,int):
                    self.typ = "num"
                    self.value = raw_data
                elif isinstance(self.raw_data,Note):
                    self.typ = "note"
                    self.value = raw_data
            else:
                self.raw_data = raw_data.strip()
                if self.raw_data[0] == "(" and self.raw_data[-1] == ")":
                    self.typ = "cycle"
                    self.value = Cycle([Data(x.strip()) for x in self.raw_data[1:-1].split(",")])

                elif self.raw_data[0] == "[" and self.raw_data[-1] == "]":
                    self.typ = "chord"
                    val = [Data(x.strip()) for x in self.raw_data[1:-1].split()]
                    if len(val) == 1:
                        self.value = Chord(val, classic_repr=True)
                    else:
                        self.value = Chord(*val)

                elif self.raw_data[0] == "{" and self.raw_data[-1] == "}":
                    self.typ = "operation"
                    self.value = Operation(*[Data(x.strip()) for x in self.raw_data[1:-1].split()])

                elif self.raw_data == "none":
                    self.typ = "none"
                    self.value = None
                    print("none")

                elif self.raw_data[0] == "@":

                    self.typ = "ref"
                    val = self.raw_data[1:].split(".")
                    if len(val) == 2:
                        self.value = Reference(val[0], val[1])
                    else:
                        self.value = Reference(val[0], None) # obsolete but still works

                elif is_note(self.raw_data):
                    self.typ = "note"
                    self.value = Note(raw_data)
                elif self.raw_data.isidentifier():
                    self.typ = "id"
                    self.value = raw_data
                elif self.raw_data.isnumeric():
                    self.typ = "num"
                    self.value = int(self.raw_data)

                elif self.raw_data in OP:
                    self.typ = "operator"
                    self.value = self.raw_data.strip()

                else:
                    raise ValueError(f"Input '{self.raw_data}' has type unknown")

    def __repr__(self):
        return f"[TYPE : '{self.typ}'  VALUE : '{self.value}']"

    def __add__(self, other):
        if self.typ == "num" and other.typ == "num":
            return Data(f"{self.value + other.value}")
        else:
            raise ValueError(f"Addition not supported for types {self.typ} and {other.typ}")

    def copy_with(self, val, typ):
        d = Data(None)
        d.typ = typ
        if typ == "note":
            d.value = Note(raw_str="c0")
            d.value.value = val
        elif typ == "num":
            d.value = val
        elif typ == "chord":
            d.value = Chord(*val)
        return d

class Note:
    def __init__(self, raw_str):
        self.raw = raw_str
        temp = [raw_str[:-1], raw_str[-1]]
        self.value = NOTES.index(temp[0]) + 12 * int(temp[1])

    def __repr__(self):
        return f"NOTE {self.raw} : {self.value}"
