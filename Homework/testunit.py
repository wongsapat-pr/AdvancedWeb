import unittest
import testfunc


class TestFunc(unittest.TestCase):
    # def test_1(self):  # House of Card
    #     self.assertEqual(testfunc.cards_needed(-3), "invalid")
    #     self.assertEqual(testfunc.cards_needed(0), 0)
    #     self.assertEqual(testfunc.cards_needed(20), 610)

    def test_2(self):  # Combined Consecutive Sequence
        self.assertEqual(testfunc.consecutive_combo([1, 4, 5, 7], [2, 3, 6]), True)
        self.assertEqual(testfunc.consecutive_combo([4, 3, 1], [0, 7, 6, 5]), False)
        self.assertEqual(testfunc.consecutive_combo([44, 46], [45]), True)

    # def test_3(self):  # Adding Numbers
    #     self.assertEqual(testfunc.add("91", "19"), "110")
    #     self.assertEqual(testfunc.add("123456789", "987654322"), "1111111111")
    #     self.assertEqual(testfunc.add("300", "3000"), "3300")
    #     self.assertEqual(testfunc.add("", "6"), "Invalid Operation")
    #     self.assertEqual(testfunc.add("", None), "Invalid Operation")

    # def test_4(self):  # Next Prime
    #     self.assertEqual(testfunc.next_prime(12), 13)
    #     self.assertEqual(testfunc.next_prime(24), 29)
    #     self.assertEqual(testfunc.next_prime(14), 17)

    # def test_5(self):  # Calculated Bonus
    #     self.assertEqual(testfunc.bonus(15), 0)
    #     self.assertEqual(testfunc.bonus(37), 1625)
    #     self.assertEqual(testfunc.bonus(50), 8200)


if __name__ == "__main__":
    unittest.main()