
import math

class Fraction:
    """Class representing a fraction and operations on it."""

    def __init__(self, num=0, den=1):
        """
        Initialize a fraction with a numerator and denominator.

        PRE :
        - `num` and `den` must be numeric types (int, float, etc.).
        - `den` must not be zero.

        POST :
        - Creates a fraction with numerator `num` and denominator `den` in reduced form.

        RAISES :
        - TypeError : If `num` or `den` are not numeric types.
        - ValueError : If `den` is zero.
        """
        if not isinstance(num, (int, float)) or not isinstance(den, (int, float)):
            raise TypeError("Numerator and denominator must be numeric.")
        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        try:
            num = int(num)
            den = int(den)
        except ValueError:
            raise TypeError("Numerator and denominator must be convertible to integers.")

        gcd = math.gcd(num, den)
        self.__numerator = num // gcd * (1 if den > 0 else -1)
        self.__denominator = abs(den) // gcd

    @property
    def numerator(self):
        """Return the numerator of the fraction."""
        return self.__numerator

    @property
    def denominator(self):
        """Return the denominator of the fraction."""
        return self.__denominator

    def __str__(self):
        """Return the reduced form of the fraction as a string."""
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else str(self.numerator)

    def __eq__(self, other):
        """Check if two fractions are equal."""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def as_mixed_number(self):
        """Return the fraction as a mixed number string."""
        whole = abs(self.numerator) // self.denominator
        remainder = (
            self.denominator - abs(self.numerator % self.denominator)
            if self.numerator < 0 and self.numerator % self.denominator != 0
            else abs(self.numerator % self.denominator)
        )
        if remainder == 0:
            return str(-whole if self.numerator < 0 else whole)
        sign = "-" if self.numerator < 0 else ""
        return f"{sign}{whole} {remainder}/{self.denominator}"

    def is_zero(self):
        """Check if the fraction is zero."""
        return self.numerator == 0

    def is_integer(self):
        """Check if the fraction is an integer."""
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the fraction is proper (< 1 in absolute value)."""
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if the fraction has a numerator of 1."""
        return self.numerator == 1
