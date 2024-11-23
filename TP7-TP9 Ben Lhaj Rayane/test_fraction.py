import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):
    """Unit tests for the Fraction class."""

    def test_initialization(self):
        """Test initialization of fractions."""
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        with self.assertRaises(ValueError):
            Fraction(1, 0)  # Denominator cannot be zero

    def test_str(self):
        """Test the string representation."""
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")
        f = Fraction(4, 1)
        self.assertEqual(str(f), "4")

    def test_as_mixed_number(self):
        """Test mixed number representation."""
        f = Fraction(7, 4)
        self.assertEqual(f.as_mixed_number(), "1 3/4")
        f = Fraction(4, 1)
        self.assertEqual(f.as_mixed_number(), "4")

    def test_addition(self):
        """Test addition of fractions."""
        f1 = Fraction(1, 4)
        f2 = Fraction(1, 2)
        result = f1 + f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

    def test_subtraction(self):
        """Test subtraction of fractions."""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

    def test_multiplication(self):
        """Test multiplication of fractions."""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 2)

    def test_division(self):
        """Test division of fractions."""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)

        with self.assertRaises(ValueError):
            f1 / Fraction(0, 1)  # Division by zero

    def test_power(self):
        """Test power of fractions."""
        f = Fraction(3, 4)
        result = f ** 2
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 16)

    def test_equality(self):
        """Test equality of fractions."""
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)  # Equivalent to 3/4
        self.assertTrue(f1 == f2)
        f3 = Fraction(2, 3)
        self.assertFalse(f1 == f3)

    def test_is_zero(self):
        """Test if the fraction is zero."""
        f = Fraction(0, 5)
        self.assertTrue(f.is_zero())
        f = Fraction(3, 4)
        self.assertFalse(f.is_zero())

    def test_is_integer(self):
        """Test if the fraction is an integer."""
        f = Fraction(4, 2)
        self.assertTrue(f.is_integer())
        f = Fraction(3, 4)
        self.assertFalse(f.is_integer())

    def test_is_proper(self):
        """Test if the fraction is proper."""
        f = Fraction(3, 4)
        self.assertTrue(f.is_proper())
        f = Fraction(5, 4)
        self.assertFalse(f.is_proper())

    def test_is_unit(self):
        """Test if the fraction is a unit fraction."""
        f = Fraction(1, 3)
        self.assertTrue(f.is_unit())
        f = Fraction(3, 4)
        self.assertFalse(f.is_unit())

    def test_is_adjacent_to(self):
        """Test if two fractions are adjacent."""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = Fraction(2, 3)
        self.assertTrue(f1.is_adjacent_to(Fraction(1, 6)))  # Différence est 1/6
        self.assertTrue(f1.is_adjacent_to(f2))  # 1/2 et 1/3 sont adjacents
        self.assertTrue(f1.is_adjacent_to(f3))  # 1/2 et 2/3 sont adjacents


if __name__ == "__main__":
    unittest.main()
