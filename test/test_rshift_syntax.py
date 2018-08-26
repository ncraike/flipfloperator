
import unittest

from flipfloperator import RshiftSyntax

from .common import IntegrationTests


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
