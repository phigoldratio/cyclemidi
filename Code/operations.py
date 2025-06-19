import random


class Operation:
    def __init__(self, left_parameter, operator, right_parameter):
        self.left_parameter = left_parameter
        self.operator = operator
        self.operator.value = self.operator.value.strip()
        self.right_parameter = right_parameter

    def evaluate(self, l, r):
        # print(f"'{self.operator}'")
        if self.operator.value == "+":
            # print("+")
            if  l.typ == "note":
                temp = l.copy_with(typ="note", val=l.value.value + r.value)
                return temp
            if l.typ == "num":
                temp = l.copy_with(typ="num", val=l.value + r.value)
                temp.value += r.value
                return temp
            if l.typ == "chord":
                temp = l.copy_with(typ="chord", val=[l.copy_with(typ="note", val=x.value.value + r.value) for x in l.value.notes])
                return temp


        elif self.operator.value == "-":
            # print("-")
            if  l.typ == "note":
                temp = l.copy_with(typ="note", val=l.value.value - r.value)
                return temp
            if l.typ == "num":
                temp = l.copy_with(typ="num", val=l.value - r.value)
                temp.value += r.value
                return temp


        elif self.operator.value == "&":
            # print("&")
            if (r.value != 0) and (r is not None):
                return l
            else:
                return r.copy_with(typ="none", val=None)

        elif self.operator.value == "#":
            if l.typ == "chord" and r.typ == "num":
                return l.value.notes[r.value]

        elif self.operator.value == "~":
            # random operator
            if r.typ == l.typ:
                if r.typ == "note":
                    return r.copy_with(typ="note", val=random.randint(l.value.value, r.value.value))
                elif r.typ == "num":
                    return r.copy_with(typ="num", val=random.randint(l.value, r.value))

        # & gate
        # # index
        # ~ octave
    def __repr__(self):
        return f"OP : {self.left_parameter} {self.operator} {self.right_parameter}"
