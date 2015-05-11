import unittest

from calculadora import Calculadora


class PruebasCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_potencia(self):
        self.assertEqual(self.calc.potencia(2,3), 8)
        self.assertEqual(self.calc.potencia(-2,3), -8)

    def test_resta(self):
        resta = self.calc.resta(10, 4)
        print "Resta:",resta
        self.assertEqual(resta, 6)

    def test_division(self):
        self.assertEqual(self.calc.division(10,5), 2)

if __name__ == "__main__":
    unittest.main()
