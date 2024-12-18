
import unittest
from implemented_fraction import Fraction

class TestFractionAdvancedFeatures(unittest.TestCase):
    """Tests pour les fonctionnalités avancées de la classe Fraction."""

    def test_as_mixed_number(self):
        """Test de la conversion en nombre mixte."""
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")  # Fraction impropre
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")  # Fraction entière
        self.assertEqual(Fraction(-7, 3).as_mixed_number(), "-2 1/3")  # Fraction négative

    def test_equality(self):
        """Test de la comparaison d'égalité."""
        self.assertTrue(Fraction(2, 4) == Fraction(1, 2))  # Fractions équivalentes
        self.assertFalse(Fraction(1, 3) == Fraction(1, 2))  # Fractions différentes

    def test_is_zero(self):
        """Test de la propriété is_zero."""
        self.assertTrue(Fraction(0, 1).is_zero())  # Fraction nulle
        self.assertFalse(Fraction(1, 2).is_zero())  # Fraction non nulle

    def test_is_integer(self):
        """Test de la propriété is_integer."""
        self.assertTrue(Fraction(4, 2).is_integer())  # Fraction entière
        self.assertFalse(Fraction(3, 2).is_integer())  # Fraction non entière

    def test_is_proper(self):
        """Test de la propriété is_proper."""
        self.assertTrue(Fraction(1, 2).is_proper())  # Fraction propre
        self.assertFalse(Fraction(5, 3).is_proper())  # Fraction impropre

    def test_is_unit(self):
        """Test de la propriété is_unit."""
        self.assertTrue(Fraction(1, 3).is_unit())  # Numérateur = 1
        self.assertFalse(Fraction(2, 3).is_unit())  # Numérateur != 1

if __name__ == "__main__":
    unittest.main()
