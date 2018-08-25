from enum import IntEnum
import unittest

class FL(IntEnum):
    OPPED = 0
    IPPED = 1

class Flipfloperator:

    def __init__(self):
        self.flipped = FL.OPPED

    def __call__(self, cond):
        if cond:
            self.flipped = FL.IPPED

        return self

    def __pow__(self, other):
        if self.flipped == FL.OPPED:
            return False

        # We were flipped until just now
        if other:
            self.flipped = FL.OPPED

        return True


class TestFlipfloperatorConstruction(unittest.TestCase):

    def test_init_should_init_flopped(self):
        ff = Flipfloperator()
        self.assertEqual(ff.flipped, FL.OPPED)


class TestFlipfloperatorMethodCall(unittest.TestCase):

    def test_call_should_return_self(self):
        ff = Flipfloperator()
        result = ff(False)
        self.assertIs(result, ff)

    def test_call_should_flip_on_true(self):
        ff = Flipfloperator()
        self.assertEqual(ff.flipped, FL.OPPED)
        ff(True)
        self.assertEqual(ff.flipped, FL.IPPED)

    def test_call_should_not_flip_on_false(self):
        ff = Flipfloperator()
        self.assertEqual(ff.flipped, FL.OPPED)
        ff(False)
        self.assertEqual(ff.flipped, FL.OPPED)


# class TestFlipfloperatorMethodPow(unittest.TestCase):
#
#     def test_pow_should_return_false_if_not_flipped()


class TestFlipfloperatorIntegration(unittest.TestCase):

    def test_flip_then_flop(self):
        ff = Flipfloperator()

    def test_a_flipping_loop(self):
        """
        Test the equivalent of the Ruby example:

            l = []
            (1..20).each do |x|
                l.push(x) if (x == 5) .. (x == 10)
            end
            # l == [5, 6, 7, 8, 9, 10]
        """

        _ = Flipfloperator()
        l = []

        for x in range(1, 20):
            l.append(x) if _(x == 5) ** (x == 10) else None

        self.assertEqual(l, [5, 6, 7, 8, 9, 10])
