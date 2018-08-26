

import unittest
from enum import IntEnum
from functools import partial
from typing import Callable, Optional


class FL(IntEnum):
    OPPED = 0
    IPPED = 1


class Flipfloperator:
    state: FL

    def __init__(self) -> None:
        self.state = FL.OPPED

    @property
    def flipped(self):
        return self.state == FL.IPPED

    @property
    def flopped(self):
        return self.state == FL.OPPED

    def flip(self):
        self.state = FL.IPPED

    def flop(self):
        self.state = FL.OPPED

    def flipfloperate(self, left: bool, right: bool) -> bool:
        if left:
            self.flip()

        if self.flopped:
            return False

        if right:
            self.flop()

        return True
