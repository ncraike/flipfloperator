
import unittest

from flipfloperator import SliceSyntax

from .common import IntegrationTests


class TestSliceSyntaxIntegration(unittest.TestCase, IntegrationTests):

    def setUp(self):
        self.slice_syntax = SliceSyntax()

    def assertFlipped(self):
        self.assertTrue(self.slice_syntax.flipfloperator.flipped)

    def assertFlopped(self):
        self.assertTrue(self.slice_syntax.flipfloperator.flopped)

    def call(self, left: bool, right: bool) -> bool:
        return self.slice_syntax[left :: right]

    def tearDown(self):
        del self.slice_syntax
