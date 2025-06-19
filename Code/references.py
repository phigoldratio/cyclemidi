

class Reference:
    def __init__(self, cycle, ref_attribute):
        self.element = cycle

    def get_ref(self, launched):
        val = None
        for va in launched.values():
            for v in va :
                if self.element in v.keys():
                    # print(list(v.values())[0])
                    val = list(v.values())[0].get_out(from_ref=True)
                    break

        return val

    def __repr__(self):
        return f"ref to {self.element}"
