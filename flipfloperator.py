

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


class RshiftSyntax:

    flipfloperator: Flipfloperator
    partial: Optional[Callable]

    def __init__(self):
        self.flipfloperator = Flipfloperator()
        self.partial = None

    def __call__(self, left: bool):
        self.partial = partial(self.flipfloperator.flipfloperate, left)
        return self

    def __rshift__(self, right: bool):
        if self.partial is None:
            raise ValueError("Call me with a boolean before using >>!")

        try:
            return self.partial(right)
        finally:
            self.partial = None


class FlipfloperatorTestCase(unittest.TestCase):

    def setUp(self):
        self.ff = Flipfloperator()

    def assertFlipped(self):
        self.assertTrue(self.ff.flipped)

    def assertFlopped(self):
        self.assertTrue(self.ff.flopped)

    def tearDown(self):
        del self.ff


class TestConstruction(FlipfloperatorTestCase):

    def test_init_should_init_flopped(self):
        self.assertFlopped()


class TestFlip(FlipfloperatorTestCase):

    def test_flip(self):
        self.ff.state = FL.OPPED
        self.ff.flip()
        self.assertFlipped()


class TestFlop(FlipfloperatorTestCase):

    def test_flop(self):
        self.ff.state = FL.IPPED
        self.ff.flop()
        self.assertFlopped()


class IntegrationTests:

    def assertFlipped(self):
        raise NotImplementedError()

    def assertFlopped(self):
        raise NotImplementedError()

    def call(self, left: bool, right: bool) -> bool:
        raise NotImplementedError()

    def test_flip_then_flop(self):
        self.assertFlopped()

        # Doesn't flip while left is False, should return False
        self.assertFalse(self.call(False, False))
        self.assertFlopped()
        self.assertFalse(self.call(False, True))
        self.assertFlopped()
        self.assertFalse(self.call(False, False))
        self.assertFlopped()

        # Flips when left is True, should now return True
        self.assertTrue(self.call(True, False))
        self.assertFlipped()
        self.assertTrue(self.call(True, False))
        self.assertFlipped()

        # Stays flipped when left is False, still returns True
        self.assertTrue(self.call(False, False))
        self.assertFlipped()
        self.assertTrue(self.call(True, False))
        self.assertFlipped()

        # Flops when right is True
        # Should return True on flop, then return False
        self.assertTrue(self.call(False, True))
        self.assertFlopped()
        self.assertFalse(self.call(False, True))

    def test_a_flipping_loop(self):
        """
        Test the equivalent of the Ruby example:

            l = []
            (1..20).each do |x|
                l.push(x) if (x == 5) .. (x == 10)
            end
            # l == [5, 6, 7, 8, 9, 10]
        """

        l = []
        for x in range(1, 20):
            if self.call(x == 5, x == 10):
                l.append(x)

        self.assertEqual(l, [5, 6, 7, 8, 9, 10])

class TestFlipfloperatorIntegration(unittest.TestCase, IntegrationTests):

    def setUp(self):
        self.flipfloperator = Flipfloperator()

    def assertFlipped(self):
        self.assertTrue(self.flipfloperator.flipped)

    def assertFlopped(self):
        self.assertTrue(self.flipfloperator.flopped)

    def call(self, left: bool, right: bool) -> bool:
        return self.flipfloperator.flipfloperate(left, right)

    def tearDown(self):
        del self.flipfloperator


class TestPowerSyntaxIntegration(unittest.TestCase, IntegrationTests):

    def setUp(self):
        self.power_syntax = PowerSyntax()

    def assertFlipped(self):
        self.assertTrue(self.power_syntax.flipfloperator.flipped)

    def assertFlopped(self):
        self.assertTrue(self.power_syntax.flipfloperator.flopped)

    def call(self, left: bool, right: bool) -> bool:
        return self.power_syntax(left) ** right

    def tearDown(self):
        del self.power_syntax


class TestRshiftSyntaxIntegration(unittest.TestCase, IntegrationTests):

    def setUp(self):
        self.rshift_syntax = RshiftSyntax()

    def assertFlipped(self):
        self.assertTrue(self.rshift_syntax.flipfloperator.flipped)

    def assertFlopped(self):
        self.assertTrue(self.rshift_syntax.flipfloperator.flopped)

    def call(self, left: bool, right: bool) -> bool:
        return self.rshift_syntax(left) >> right

    def tearDown(self):
        del self.rshift_syntax
