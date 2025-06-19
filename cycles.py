from numpy import mod

from data import *

class Cycle:
    def __init__(self, values, speed=1, loop=True, reboot=False):
        self.values = values
        self.speed = speed
        self.loop = loop
        self.reboot = reboot
        self.clock = 0

    def get_out(self, from_ref=False):

        val = self.values[((self.clock // self.speed) % len(self.values))]
        if self.clock % self.speed != 0 and not from_ref:
            return None
        return val

    def update_time(self):
        self.clock += 1
        if self.reboot and self.clock >= GLOBAL_CYCLE * SUBD:
            self.clock = 0

    def __repr__(self):
        return f'cycle : {self.values} / {self.speed}'
