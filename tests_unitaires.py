import unittest
import math
from implemented_fraction import Fraction  # Remplacez par le nom de votre fichier


class TestFraction(unittest.TestCase):

    def test_constructor(self):
        """Test du constructeur de la classe Fraction"""
        # Cas normal
        f = Fraction(1, 2)
        self.assertEqual(str(f), "1/2")  # La fraction doit être réduite correctement

        # Cas : Fraction entière
        f = Fraction(10, 5)
        self.assertEqual(str(f), "2")

        # Cas : Fraction négative
        f = Fraction(-4, 5)
        self.assertEqual(str(f), "-4/5")

        # Cas : Dénominateur négatif
        f = Fraction(4, -5)
        self.assertEqual(str(f), "-4/5")

        # Cas : Dénominateur nul (doit lever une exception)
        with self.assertRaises(ValueError):
            Fraction(1, 0)

        # Cas : Fraction nulle
        f = Fraction(0, 5)
        self.assertEqual(str(f), "0")

    def test_str(self):
        """Test de la méthode __str__"""
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(3, 1)), "3")  # Fraction entière
        self.assertEqual(str(Fraction(-1, 3)), "-1/3")  # Fraction négative

    def test_as_mixed_number(self):
        """Test de la méthode as_mixed_number"""
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")  # Fraction impropre
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")  # Fraction entière
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "1/2")  # Fraction propre

    def test_addition(self):
        """Test de l'addition de fractions"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertEqual(str(f1 + f2), "5/4")  # Mise au même dénominateur

        f3 = Fraction(-1, 4)
        self.assertEqual(str(f1 + f3), "1/4")  # Avec une fraction négative

    def test_division(self):
        """Test de la division de fractions"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertEqual(str(f2 / f1), "3/2")  # Division classique

        # Division par une fraction nulle (doit lever une exception)
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_equality(self):
        """Test de la méthode __eq__"""
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))  # Fractions équivalentes
        self.assertFalse(Fraction(1, 3) == Fraction(1, 2))  # Fractions différentes

    def test_is_integer(self):
        """Test de la méthode is_integer"""
        self.assertTrue(Fraction(4, 2).is_integer())  # Fraction entière
        self.assertFalse(Fraction(3, 2).is_integer())  # Pas un entier

    def test_is_proper(self):
        """Test de la méthode is_proper"""
        self.assertTrue(Fraction(1, 2).is_proper())  # Fraction propre
        self.assertFalse(Fraction(3, 2).is_proper())  # Fraction impropre

    def test_is_adjacent_to(self):
        """Test de la méthode is_adjacent_to"""
        f1 = Fraction(1, 3)
        f2 = Fraction(2, 3)
        self.assertTrue(f1.is_adjacent_to(f2))  # Adjacentes
        f3 = Fraction(3, 4)
        self.assertFalse(f1.is_adjacent_to(f3))  # Non adjacentes
    def test_subtraction(self):
        """Test de la soustraction de fractions"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        self.assertEqual(str(f1 - f2), "1/2")  # Soustraction classique
        f3 = Fraction(1, 4)
        f4 = Fraction(3, 4)
        self.assertEqual(str(f3 - f4), "-1/2")  # Résultat négatif

    def test_multiplication(self):
        """Test de la multiplication de fractions"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(str(f1 * f2), "1/2")  # Multiplication classique
        f3 = Fraction(0, 1)
        self.assertEqual(str(f1 * f3), "0")  # Multiplication par zéro

    def test_power(self):
        """Test de l'exponentiation des fractions"""
        f = Fraction(1, 2)
        self.assertEqual(str(f ** 2), "1/4")  # Puissance positive
        self.assertEqual(str(f ** 0), "1")  # Puissance nulle
        self.assertEqual(str(f ** -1), "2")  # Puissance négative (inverse)

    def test_float_conversion(self):
        """Test de la conversion en float"""
        f1 = Fraction(1, 2)
        self.assertEqual(float(f1), 0.5)  # Conversion classique
        f2 = Fraction(2, 3)
        self.assertAlmostEqual(float(f2), 0.666666666, places=6)  # Conversion avec approximation

    def test_is_zero(self):
        """Test de la méthode is_zero"""
        f1 = Fraction(0, 5)
        self.assertTrue(f1.is_zero())  # Fraction nulle
        f2 = Fraction(3, 5)
        self.assertFalse(f2.is_zero())  # Fraction non nulle

    def is_unit(self):
        """Vérifie si une fraction est unitaire (numérateur égal à 1 après réduction)."""
        gcd = math.gcd(self.numerator, self.denominator)
        reduced_numerator = self.numerator // gcd
        reduced_denominator = self.denominator // gcd
        return reduced_numerator == 1 and reduced_denominator > 0



