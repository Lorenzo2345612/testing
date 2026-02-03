import unittest
from edad import mensaje_edad


class TestMensajeEdad(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Iniciando tests de mensaje_edad")
    
    @classmethod
    def tearDownClass(cls):
        print("\nFinalizando tests de mensaje_edad")
    
    def test_edad_negativa(self):
        """Probando con una persona con menos de 0 años"""
        resultado = mensaje_edad(-5)
        self.assertEqual(resultado, 'No existes')
    
    def test_edad_nino(self):
        """Probando con una persona de 3 años"""
        resultado = mensaje_edad(3)
        self.assertEqual(resultado, 'Eres un niño')
    
    def test_edad_adolescente(self):
        """Probando con una persona de 15 años"""
        resultado = mensaje_edad(15)
        self.assertEqual(resultado, 'Eres un adolescente')
    
    def test_edad_adulto(self):
        """Probando con una persona de 64 años"""
        resultado = mensaje_edad(64)
        self.assertEqual(resultado, 'Eres un adulto')
    
    def test_edad_adulto_mayor(self):
        """Probando con una persona de 110 años"""
        resultado = mensaje_edad(110)
        self.assertEqual(resultado, 'Eres un adulto mayor')
    
    def test_edad_mumm_ra(self):
        """Probando con una persona de 120 años"""
        resultado = mensaje_edad(120)
        self.assertEqual(resultado, 'Eres Mumm-Ra')
    
    def test_edad_no_numerica_string(self):
        """Probando con una edad no numerica"""
        resultado = mensaje_edad("veinte")
        self.assertEqual(resultado, 'Edad no válida')
    
    def test_edad_no_numerica_float(self):
        """Probando con 17.45 años"""
        resultado = mensaje_edad(17.45)
        self.assertEqual(resultado, 'Edad no válida')


if __name__ == '__main__':
    unittest.main()
