
import unittest

from flipfloperator import FL, Flipfloperator

from .common import IntegrationTests


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


class TestFlipfloperatorCallSyntaxIntegration(unittest.TestCase, IntegrationTests):

    def setUp(self):
        self.flipfloperator = Flipfloperator()

    def assertFlipped(self):
        self.assertTrue(self.flipfloperator.flipped)

    def assertFlopped(self):
        self.assertTrue(self.flipfloperator.flopped)

    def call(self, left: bool, right: bool) -> bool:
        return self.flipfloperator(left, right)

    def tearDown(self):
        del self.flipfloperator
