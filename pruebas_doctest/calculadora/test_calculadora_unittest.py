import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Iniciando tests de la calculadora")
        cls.calc = Calculadora()

    @classmethod
    def tearDownClass(cls):
        print("Finalizando tests de la calculadora")
    
    # Tests para el método sumar
    def test_sumar_con_texto(self):
        """Se ingresa el número 2 y la letra 'X', debe devolver 'Sólo se aceptan números'"""
        resultado = self.calc.sumar(2, 'X')
        self.assertEqual(resultado, 'Sólo se aceptan números')
    
    def test_sumar_numeros_negativos(self):
        """Se ingresa el número -2 y el número 5, debe devolver 'Sólo se pueden sumar números positivos'"""
        resultado = self.calc.sumar(-2, 5)
        self.assertEqual(resultado, 'Sólo se pueden sumar números positivos')
    
    def test_sumar_numeros_decimales(self):
        """Se ingresa el número 2 y el número 0.5, debe devolver 'Sólo se pueden sumar números enteros'"""
        resultado = self.calc.sumar(2, 0.5)
        self.assertEqual(resultado, 'Sólo se pueden sumar números enteros')
    
    def test_sumar_numeros_positivos_enteros(self):
        """Se ingresa el número 2 y el número 5, debe devolver 7"""
        resultado = self.calc.sumar(2, 5)
        self.assertEqual(resultado, 7)
    
    # Tests para el método restar
    def test_restar_con_texto(self):
        """Se ingresa el número 2 y la letra 'X', debe devolver 'Sólo se aceptan números'"""
        resultado = self.calc.restar(2, 'X')
        self.assertEqual(resultado, 'Sólo se aceptan números')
    
    def test_restar_numeros_negativos(self):
        """Se ingresa el número -2 y el número 5, debe devolver 'Sólo se pueden restar números positivos'"""
        resultado = self.calc.restar(-2, 5)
        self.assertEqual(resultado, 'Sólo se pueden restar números positivos')
    
    def test_restar_numeros_decimales(self):
        """Se ingresa el número 2 y el número 0.5, debe devolver 'Sólo se pueden restar números enteros'"""
        resultado = self.calc.restar(2, 0.5)
        self.assertEqual(resultado, 'Sólo se pueden restar números enteros')
    
    def test_restar_numeros_positivos_enteros(self):
        """Se ingresa el número 7 y el número 5, debe devolver 2"""
        resultado = self.calc.restar(7, 5)
        self.assertEqual(resultado, 2)
    
    # Tests para el método multiplicar
    def test_multiplicar_con_texto(self):
        """Se ingresa el número 2 y la letra 'X', debe devolver 'Sólo se aceptan números'"""
        resultado = self.calc.multiplicar(2, 'X')
        self.assertEqual(resultado, 'Sólo se aceptan números')
    
    def test_multiplicar_numeros_negativos(self):
        """Se ingresa el número -2 y el número 5, debe devolver 'Sólo se pueden multiplicar números positivos'"""
        resultado = self.calc.multiplicar(-2, 5)
        self.assertEqual(resultado, 'Sólo se pueden multiplicar números positivos')
    
    def test_multiplicar_numeros_decimales(self):
        """Se ingresa el número 2 y el número 0.5, debe devolver 'Sólo se pueden multiplicar números enteros'"""
        resultado = self.calc.multiplicar(2, 0.5)
        self.assertEqual(resultado, 'Sólo se pueden multiplicar números enteros')
    
    def test_multiplicar_numeros_positivos_enteros(self):
        """Se ingresa el número 2 y el número 5, debe devolver 10"""
        resultado = self.calc.multiplicar(2, 5)
        self.assertEqual(resultado, 10)
    
    # Tests para el método dividir
    def test_dividir_con_texto(self):
        """Se ingresa el número 2 y la letra 'X', debe devolver 'Sólo se aceptan números'"""
        resultado = self.calc.dividir(2, 'X')
        self.assertEqual(resultado, 'Sólo se aceptan números')
    
    def test_dividir_numeros_negativos(self):
        """Se ingresa el número -2 y el número 5, debe devolver 'Sólo se pueden dividir números positivos'"""
        resultado = self.calc.dividir(-2, 5)
        self.assertEqual(resultado, 'Sólo se pueden dividir números positivos')
    
    def test_dividir_numeros_decimales(self):
        """Se ingresa el número 2 y el número 0.5, debe devolver 'Sólo se pueden dividir números enteros'"""
        resultado = self.calc.dividir(2, 0.5)
        self.assertEqual(resultado, 'Sólo se pueden dividir números enteros')
    
    def test_dividir_entre_cero(self):
        """Se ingresa el número 2 y el número 0, debe devolver 'No se puede dividir entre cero'"""
        resultado = self.calc.dividir(2, 0)
        self.assertEqual(resultado, 'No se puede dividir entre cero')
    
    def test_dividir_numeros_positivos_enteros(self):
        """Se ingresa el número 10 y el número 5, debe devolver 2.0"""
        resultado = self.calc.dividir(10, 5)
        self.assertEqual(resultado, 2.0)
    
    # Tests para el método potencia
    def test_potencia_con_texto(self):
        """Se ingresa el número 2 y la letra 'X', debe devolver 'Sólo se aceptan números'"""
        resultado = self.calc.potencia(2, 'X')
        self.assertEqual(resultado, 'Sólo se aceptan números')
    
    def test_potencia_numeros_negativos(self):
        """Se ingresa el número -2 y el número 5, debe devolver 'Sólo se pueden elevar a potencia números positivos'"""
        resultado = self.calc.potencia(-2, 5)
        self.assertEqual(resultado, 'Sólo se pueden elevar a potencia números positivos')
    
    def test_potencia_numeros_decimales(self):
        """Se ingresa el número 2 y el número 0.5, debe devolver 'Sólo se pueden elevar a potencia números enteros'"""
        resultado = self.calc.potencia(2, 0.5)
        self.assertEqual(resultado, 'Sólo se pueden elevar a potencia números enteros')
    
    def test_potencia_numeros_positivos_enteros(self):
        """Se ingresa el número 2 y el número 5, debe devolver 32"""
        resultado = self.calc.potencia(2, 5)
        self.assertEqual(resultado, 32)
    
    # Tests para el método raiz
    def test_raiz_con_texto(self):
        """Se ingresa el número 2 y la letra 'X', debe devolver 'Sólo se aceptan números'"""
        resultado = self.calc.raiz(2, 'X')
        self.assertEqual(resultado, 'Sólo se aceptan números')
    
    def test_raiz_numeros_negativos(self):
        """Se ingresa el número -2 y el número 5, debe devolver 'Sólo se pueden calcular raíces de números positivos'"""
        resultado = self.calc.raiz(-2, 5)
        self.assertEqual(resultado, 'Sólo se pueden calcular raíces de números positivos')
    
    def test_raiz_numeros_decimales(self):
        """Se ingresa el número 2 y el número 0.5, debe devolver 'Sólo se pueden calcular raíces de números enteros'"""
        resultado = self.calc.raiz(2, 0.5)
        self.assertEqual(resultado, 'Sólo se pueden calcular raíces de números enteros')
    
    def test_raiz_numeros_positivos_enteros(self):
        """Se ingresa el número 32 y el número 5, debe devolver 2.0"""
        resultado = self.calc.raiz(32, 5)
        self.assertEqual(resultado, 2.0)


if __name__ == '__main__':
    unittest.main()
