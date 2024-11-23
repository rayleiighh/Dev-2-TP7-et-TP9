from math import gcd
from typing import Union


class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """Initialize a fraction with a numerator and a denominator.

        PRE: den != 0, num and den are integers
        POST: Fraction is stored in reduced form.
        RAISES: ValueError if den == 0.
                TypeError if num or den is not an integer.
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Numerator and denominator must be integers.")
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        self._num = num
        self._den = den
        self._reduce()

    def _reduce(self):
        """Reduce the fraction to its simplest form."""
        divisor = gcd(self._num, self._den)
        self._num //= divisor
        self._den //= divisor
        if self._den < 0:  # Keep the denominator positive
            self._num = -self._num
            self._den = -self._den

    @property
    def numerator(self) -> int:
        """Return the numerator of the fraction."""
        return self._num

    @property
    def denominator(self) -> int:
        """Return the denominator of the fraction."""
        return self._den

    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Return a textual representation of the reduced form of the fraction.

        POST: Returns "numerator/denominator" or "numerator" if denominator is 1.
        """
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def as_mixed_number(self) -> str:
        """Return a textual representation of the fraction as a mixed number.

        POST: Returns a string representation of the mixed number.
        """
        whole = self._num // self._den
        remainder = abs(self._num % self._den)
        if remainder == 0:
            return str(whole)
        if whole == 0:
            return f"{remainder}/{self._den}"
        return f"{whole} {remainder}/{self._den}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other: Union['Fraction', int]) -> 'Fraction':
        """Overload the + operator for fractions.

        PRE: other must be a Fraction or int.
        POST: Returns a new Fraction representing the sum.
        RAISES: TypeError if other is not a Fraction or int.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Can only add Fraction or int with Fraction.")
        num = self._num * other.denominator + other.numerator * self._den
        den = self._den * other.denominator
        return Fraction(num, den)

    def __sub__(self, other: Union['Fraction', int]) -> 'Fraction':
        """Overload the - operator for fractions.

        PRE: other must be a Fraction or int.
        POST: Returns a new Fraction representing the difference.
        RAISES: TypeError if other is not a Fraction or int.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract Fraction or int with Fraction.")
        num = self._num * other.denominator - other.numerator * self._den
        den = self._den * other.denominator
        return Fraction(num, den)

    def __mul__(self, other: Union['Fraction', int]) -> 'Fraction':
        """Overload the * operator for fractions.

        PRE: other must be a Fraction or int.
        POST: Returns a new Fraction representing the product.
        RAISES: TypeError if other is not a Fraction or int.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply Fraction or int with Fraction.")
        num = self._num * other.numerator
        den = self._den * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other: Union['Fraction', int]) -> 'Fraction':
        """Overload the / operator for fractions.

        PRE: other must be a Fraction or int and cannot be zero.
        POST: Returns a new Fraction representing the quotient.
        RAISES: TypeError if other is not a Fraction or int.
                ValueError if dividing by zero.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide Fraction or int with Fraction.")
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        num = self._num * other.denominator
        den = self._den * other.numerator
        return Fraction(num, den)

    def __pow__(self, power: int) -> 'Fraction':
        """Overload the ** operator for fractions.

        PRE: power must be an integer.
        POST: Returns a new Fraction representing the fraction raised to the power.
        RAISES: TypeError if power is not an integer.
        """
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")
        num = self._num**power
        den = self._den**power
        return Fraction(num, den)

    def __eq__(self, other: Union['Fraction', int]) -> bool:
        """Overload the == operator for fractions.

        PRE: other must be a Fraction or int.
        POST: Returns True if fractions are equal, False otherwise.
        RAISES: TypeError if other is not a Fraction or int.
        """
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction or int with Fraction.")
        return self._num == other.numerator and self._den == other.denominator

    def __float__(self) -> float:
        """Return the decimal value of the fraction.

        POST: Returns the fraction's decimal value as a float.
        """
        return self._num / self._den

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Check if the fraction's value is 0.

        POST: Returns True if the fraction is 0, False otherwise.
        """
        return self._num == 0

    def is_integer(self) -> bool:
        """Check if the fraction is an integer.

        POST: Returns True if the fraction is an integer, False otherwise.
        """
        return self._num % self._den == 0

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1.

        POST: Returns True if the fraction is proper, False otherwise.
        """
        return abs(self._num) < abs(self._den)

    def is_unit(self) -> bool:
        """Check if the fraction's numerator is 1 in its reduced form.

        POST: Returns True if the fraction is a unit fraction, False otherwise.
        """
        return abs(self._num) == 1 and self._den != 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Check if two fractions differ by a unit fraction.

        PRE: other must be a Fraction.
        POST: Returns True if fractions differ by a unit fraction, False otherwise.
        RAISES: TypeError if other is not a Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with another Fraction.")

        # Compute the difference
        diff = self - other

        # Check if the absolute value of the difference is a unit fraction
        return abs(diff.numerator) == 1 and diff.denominator > 0
