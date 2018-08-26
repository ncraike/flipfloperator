
import unittest

from flipfloperator import PowerSyntax

from .common import IntegrationTests


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
