import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
            Configuración inicial para los tests.
        """
        print("Iniciando tests para la función factorial.")

    @classmethod
    def tearDownClass(cls):
        """
            Limpieza después de los tests.
        """
        print("Finalizando tests para la función factorial.")
    
    def test_factorial_1(self):
        """
            Test para el factorial de 1.
        """
        resultado = factorial(1)
        self.assertEqual(resultado, 1)

    def test_factorial_5(self):
        """
            Test para el factorial de 5.
        """
        resultado = factorial(5)
        self.assertEqual(resultado, 120)
    
    def test_factorial_0(self):
        """
            Test para el factorial de 0.
        """
        resultado = factorial(0)
        self.assertEqual(resultado, 1)

    def test_factorial_10(self):
        """
            Test para el factorial de 10.
        """
        resultado = factorial(10)
        self.assertEqual(resultado, 3628800)
    
    def test_factorial_negativo(self):
        """
            Test para el factorial de un número negativo.
        """
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_factorial_no_entero(self):
        """
            Test para el factorial de un número no entero.
        """
        with self.assertRaises(TypeError):
            factorial(4.5)

    def test_factorial_no_numero(self):
        """
            Test para el factorial de un valor no numérico.
        """
        with self.assertRaises(TypeError):
            factorial("texto")

if __name__ == '__main__':
    unittest.main()



        
