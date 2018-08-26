"""
Support flipfloperating with `**` syntax.


"""

from functools import partial
from typing import Callable, Optional

from .core import Flipfloperator


class PowerSyntax:

    flipfloperator: Flipfloperator
    partial: Optional[Callable]

    def __init__(self):
        self.flipfloperator = Flipfloperator()
        self.partial = None

    def __call__(self, left: bool):
        self.partial = partial(self.flipfloperator.flipfloperate, left)
        return self

    def __pow__(self, right: bool):
        if self.partial is None:
            raise ValueError("Call me with a boolean before using **!")

        try:
            return self.partial(right)
        finally:
            self.partial = None
