import unittest
import custom_factorial


class TestStringMethods(unittest.TestCase):

    def test_int_vals(self):
        self.assertEqual(custom_factorial.factorial(3), 6)
        self.assertEqual(custom_factorial.factorial(4), 24)
        self.assertEqual(custom_factorial.factorial(6), 720)

    def test_fp_vals(self):
        self.assertRaises(
                          ValueError,
                          custom_factorial.factorial(5.3),
                          msg='Факториала от дробного числа не существует!'
                         )

    def test_invalid_vals(self):
        pass


if __name__ == '__main__':
    unittest.main()
