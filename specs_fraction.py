class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : `den` must be non-zero.
        POST : Creates a fraction with numerator `num` and denominator `den`,
               stored in reduced form.
        """
        pass

    @property
    def numerator(self):
        """Return the numerator of the fraction."""
        pass

    @property
    def denominator(self):
        """Return the denominator of the fraction."""
        pass

# ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None
        POST : Returns a string in the form "num/den" if the fraction is not an integer,
               otherwise returns the integer as a string.
        """
        pass

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None
        POST : Returns a string in the form "integer proper_fraction" where `proper_fraction` is "num/den"
               or just "integer" if there is no proper fraction part.
        """
        pass


# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : `other` must be an instance of `Fraction`.
         POST : Returns a new `Fraction` representing the sum of `self` and `other`.
         """
        pass

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : `other` must be an instance of `Fraction`.
        POST : Returns a new `Fraction` representing the difference of `self` and `other`.
        """
        pass

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : `other` must be an instance of `Fraction`.
        POST : Returns a new `Fraction` representing the product of `self` and `other`.
        """
        pass

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : `other` must be an instance of `Fraction` and `other`'s numerator must not be zero.
        POST : Returns a new `Fraction` representing the quotient of `self` divided by `other`.
        """
        pass

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : `other` must be an integer.
        POST : Returns a new `Fraction` representing `self` raised to the power of `other`.
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : `other` must be an instance of `Fraction`.
        POST : Returns `True` if `self` and `other` represent the same fraction, otherwise `False`.
        """
        pass

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None
        POST : Returns a float representing the decimal value of the fraction.
        """
        pass

# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None
        POST : Returns `True` if the numerator of the fraction is 0, otherwise `False`.
        """
        pass

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None
        POST : Returns `True` if the fraction reduces to an integer, otherwise `False`.
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None
        POST : Returns `True` if the absolute value of the fraction is less than 1, otherwise `False`.
        """
        pass

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None
        POST : Returns `True` if the numerator of the fraction is 1 in reduced form, otherwise `False`.
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference is a unit fraction.

        PRE : `other` must be an instance of `Fraction`.
        POST : Returns `True` if `self` and `other` differ by a unit fraction, otherwise `False`.
        """
        pass
