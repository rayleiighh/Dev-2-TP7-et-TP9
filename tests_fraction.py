
from implemented_fraction  import Fraction

def main():
    try:
        # Création de fractions
        f1 = Fraction(1, 2)  # 1/2
        f2 = Fraction(3, 4)  # 3/4
        f3 = Fraction(0, 5)  # 0/5

        print("Fraction 1:", f1)
        print("Fraction 2:", f2)
        print("Fraction 3:", f3)

        # Test des propriétés
        print("f1 is zero:", f1.is_zero())
        print("f3 is zero:", f3.is_zero())
        print("f2 is integer:", f2.is_integer())
        print("f3 is proper:", f3.is_proper())

        # Test des opérateurs arithmétiques
        f4 = f1 + f2
        f5 = f2 - f1
        f6 = f1 * f2
        f7 = f2 / f1

        print("f1 + f2 =", f4)
        print("f2 - f1 =", f5)
        print("f1 * f2 =", f6)
        print("f2 / f1 =", f7)

        # Test d'autres opérations
        f8 = f1 ** 2
        print("f1 ** 2 =", f8)

        # Comparaison et conversion
        print("f1 == f2:", f1 == f2)
        print("f1 as float:", float(f1))

        # Test de la méthode as_mixed_number
        f9 = Fraction(7, 3)
        print("Fraction 9 as mixed number:", f9.as_mixed_number())

        # Test d'exceptions
        try:
            f10 = Fraction(1, 0)  # Denominator cannot be zero
        except ValueError as e:
            print("Caught exception:", e)

        # Test de fractions adjacentes
        f11 = Fraction(1, 3)
        f12 = Fraction(2, 3)
        print("f11 is adjacent to f12:", f11.is_adjacent_to(f12))

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
