import unittest
from numero_a_letra import numero_a_letra


class TestNumeroALetra(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Iniciando tests de número a letra")

    @classmethod
    def tearDownClass(cls):
        print("\nFinalizando tests de número a letra")

    def test_convertir_1(self):
        """Prueba para convertir 1 a letra"""
        resultado = numero_a_letra(1)
        self.assertEqual(resultado, 'uno')

    def test_convertir_11(self):
        """Prueba para convertir 11 a letra"""
        resultado = numero_a_letra(11)
        self.assertEqual(resultado, 'once')

    def test_convertir_31(self):
        """Prueba para convertir 31 a letra"""
        resultado = numero_a_letra(31)
        self.assertEqual(resultado, 'treinta y uno')

    def test_convertir_25(self):
        """Prueba para convertir 25 a letra"""
        resultado = numero_a_letra(25)
        self.assertEqual(resultado, 'veinticinco')

    def test_convertir_353(self):
        """Prueba para convertir 353 a letra"""
        resultado = numero_a_letra(353)
        self.assertEqual(resultado, 'trescientos cincuenta y tres')

    def test_convertir_325(self):
        """Prueba para convertir 325 a letra"""
        resultado = numero_a_letra(325)
        self.assertEqual(resultado, 'trescientos veinticinco')

    def test_convertir_100(self):
        """Prueba para convertir 100 a letra"""
        resultado = numero_a_letra(100)
        self.assertEqual(resultado, 'cien')

    def test_convertir_101(self):
        """Prueba para convertir 101 a letra"""
        resultado = numero_a_letra(101)
        self.assertEqual(resultado, 'ciento uno')

    def test_convertir_569(self):
        """Prueba para convertir 569 a letra"""
        resultado = numero_a_letra(569)
        self.assertEqual(resultado, 'quinientos sesenta y nueve')

    def test_convertir_1000(self):
        """Prueba para convertir 1000 a letra"""
        resultado = numero_a_letra(1000)
        self.assertEqual(resultado, 'mil')

    def test_convertir_2000(self):
        """Prueba para convertir 2000 a letra"""
        resultado = numero_a_letra(2000)
        self.assertEqual(resultado, 'dos mil')

    def test_convertir_30245(self):
        """Prueba para convertir 30245 a letra"""
        resultado = numero_a_letra(30245)
        self.assertEqual(resultado, 'treinta mil doscientos cuarenta y cinco')

    def test_convertir_100000(self):
        """Prueba para convertir 100000 a letra"""
        resultado = numero_a_letra(100000)
        self.assertEqual(resultado, 'cien mil')

    def test_convertir_200000(self):
        """Prueba para convertir 200000 a letra"""
        resultado = numero_a_letra(200000)
        self.assertEqual(resultado, 'doscientos mil')

    def test_convertir_325569(self):
        """Prueba para convertir 325569 a letra"""
        resultado = numero_a_letra(325569)
        self.assertEqual(resultado, 'trescientos veinticinco mil quinientos '
                         'sesenta y nueve')

    def test_convertir_1000000(self):
        """Prueba para convertir 1000000 a letra"""
        resultado = numero_a_letra(1000000)
        self.assertEqual(resultado, 'un millón')

    def test_convertir_2000000(self):
        """Prueba para convertir 2000000 a letra"""
        resultado = numero_a_letra(2000000)
        self.assertEqual(resultado, 'dos millones')

    def test_convertir_3255691(self):
        """Prueba para convertir 3255691 a letra"""
        resultado = numero_a_letra(3255691)
        self.assertEqual(resultado, 'tres millones doscientos cincuenta y '
                         'cinco mil seiscientos noventa y uno')

    def test_convertir_0_55(self):
        """Prueba para convertir 0.55 a letra"""
        resultado = numero_a_letra(0.55)
        self.assertEqual(resultado, 'cero con cincuenta y cinco centavos')

    def test_convertir_1_01(self):
        """Prueba para convertir 1.01 a letra"""
        resultado = numero_a_letra(1.01)
        self.assertEqual(resultado, 'un con un centavo')

    def test_convertir_123456789_99(self):
        """Prueba para convertir 123456789.99 a letra"""
        resultado = numero_a_letra(123456789.99)
        self.assertEqual(resultado, 'ciento veintitrés millones cuatrocientos '
                         'cincuenta y seis mil setecientos ochenta y nueve '
                         'con noventa y nueve centavos')

    def test_convertir_1000000000(self):
        """Prueba para convertir 1000000000 a letra"""
        resultado = numero_a_letra(1000000000)
        self.assertEqual(resultado, 'mil millones')

    def test_convertir_1000000001_fuera_rango(self):
        """Prueba para convertir 1000000001 a letra (fuera de rango)"""
        resultado = numero_a_letra(1000000001)
        self.assertEqual(resultado, 'Error: Número fuera de rango')

    def test_convertir_negativo_5_fuera_rango(self):
        """Prueba para convertir -5 a letra (fuera de rango)"""
        resultado = numero_a_letra(-5)
        self.assertEqual(resultado, 'Error: Número fuera de rango')

    def test_convertir_texto_entrada_invalida(self):
        """Prueba para convertir "texto" a letra (entrada inválida)"""
        resultado = numero_a_letra("texto")
        self.assertEqual(resultado, 'Error: Entrada inválida')

    def test_convertir_121000_75(self):
        """Prueba para convertir 121000.75 a letra"""
        resultado = numero_a_letra(121000.75)
        self.assertEqual(resultado, 'ciento veintiún mil con setenta y '
                         'cinco centavos')

    def test_convertir_121000000_34(self):
        """Prueba para convertir 121000000.34 a letra"""
        resultado = numero_a_letra(121000000.34)
        self.assertEqual(resultado, 'ciento veintiún millones con treinta y '
                         'cuatro centavos')

    def test_convertir_cadena_vacia(self):
        """Prueba para convertir "" a letra (entrada inválida)"""
        resultado = numero_a_letra("")
        self.assertEqual(resultado, 'Error: Entrada inválida')

    def test_convertir_negativo_10_fuera_rango(self):
        """Prueba para convertir -10 a letra (fuera de rango)"""
        resultado = numero_a_letra(-10)
        self.assertEqual(resultado, 'Error: Número fuera de rango')


if __name__ == '__main__':
    unittest.main()
