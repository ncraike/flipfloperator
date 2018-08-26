

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
