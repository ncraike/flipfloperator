"""
Support flipfloperating with `[ :: ]` syntax.


"""

from functools import partial
from typing import Callable, Optional

from .core import Flipfloperator


class SliceSyntax:

    flipfloperator: Flipfloperator
    partial: Optional[Callable]

    def __init__(self):
        self.flipfloperator = Flipfloperator()

    def __getitem__(self, slice: slice):
        left, middle, right = slice.start, slice.stop, slice.step

        return self.flipfloperator(left, right)
