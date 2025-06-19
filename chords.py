class Chord:
    def __init__(self, *notes, classic_repr=False):
        self.notes = notes

    def __repr__(self):
        val = ""
        for note in self.notes:
            val += "  " + note.__repr__()
        return f"chord : {val}"
