import math

class Fraction:
    """Class representing a fraction and operations on it"""

    def __init__(self, num=0, den=1):
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        gcd = math.gcd(num, den)
        self._numerator = num // gcd * (1 if den > 0 else -1)
        self._denominator = abs(den) // gcd

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __str__(self):
        """Représentation textuelle d'une fraction réduite."""
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else str(self.numerator)

    def as_mixed_number(self):
        """Représentation textuelle d'une fraction sous forme de nombre mixte."""
        whole = self.numerator // self.denominator
        remainder = self.numerator % self.denominator
        if remainder == 0:
            return str(whole)
        return f"{whole} {abs(remainder)}/{self.denominator}" if whole != 0 else f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Additionne deux fractions."""
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """Soustrait deux fractions."""
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        """Multiplie deux fractions."""
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        """Divise deux fractions."""
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __pow__(self, power):
        """Élève une fraction à une puissance entière."""
        if power < 0:
            return Fraction(self.denominator ** abs(power), self.numerator ** abs(power))
        return Fraction(self.numerator ** power, self.denominator ** power)

    def __eq__(self, other):
        """Teste l'égalité entre deux fractions."""
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Retourne la valeur décimale de la fraction."""
        return self.numerator / self.denominator

    def is_zero(self):
        """Vérifie si la fraction vaut zéro."""
        return self.numerator == 0

    def is_integer(self):
        """Vérifie si la fraction est un entier."""
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Vérifie si la fraction est propre (< 1 en valeur absolue)."""
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Vérifie si la fraction a un numérateur égal à 1 (forme réduite)."""
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Vérifie si deux fractions sont adjacentes (diffèrent d'une fraction unitaire)."""
        diff_num = abs(self.numerator * other.denominator - other.numerator * self.denominator)
        diff_den = self.denominator * other.denominator

        # Réduire la fraction résultante
        gcd = math.gcd(diff_num, diff_den)
        reduced_num = diff_num // gcd
        reduced_den = diff_den // gcd

        # Vérifier si la fraction réduite est une fraction unitaire
        return reduced_num == 1 and reduced_den > 0






