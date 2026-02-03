import unittest
from partido_tenis import PartidoTenis


class TestPartidoTenis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nIniciando pruebas de PartidoTenis")

    @classmethod
    def tearDownClass(cls):
        print("\nFinalizando pruebas de PartidoTenis")

    def setUp(self):
        self.partido = PartidoTenis()

    def tearDown(self):
        self.partido = None

    def test_gana_jugador_1(self):
        """Prueba gana jugador 1"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        resultado = self.partido.score()
        self.assertEqual(resultado, 'Game | -')

    def test_gana_jugador_2(self):
        """Prueba gana jugador 2"""
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        resultado = self.partido.score()
        self.assertEqual(resultado, '- | Game')

    def test_empate_40_deuce(self):
        """Prueba empate a 40 (deuce)"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        resultado = self.partido.score()
        self.assertEqual(resultado, 'Deuce')

    def test_ventaja_jugador_1(self):
        """Prueba ventaja jugador 1"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 1")
        resultado = self.partido.score()
        self.assertEqual(resultado, 'Adv | -')

    def test_ventaja_jugador_2(self):
        """Prueba ventaja jugador 2"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        resultado = self.partido.score()
        self.assertEqual(resultado, '- | Adv')

    def test_gana_jugador_1_tras_ventaja(self):
        """Prueba gana jugador 1 tras ventaja"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        resultado = self.partido.score()
        self.assertEqual(resultado, 'Game | -')

    def test_gana_jugador_2_tras_ventaja(self):
        """Prueba gana jugador 2 tras ventaja"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        resultado = self.partido.score()
        self.assertEqual(resultado, '- | Game')

    def test_secuencia_larga(self):
        """Prueba secuencia larga"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        resultado = self.partido.score()
        self.assertEqual(resultado, 'Game | -')

    def test_15_0(self):
        """Prueba 15 | 0"""
        self.partido.point_won_by("jugador 1")
        resultado = self.partido.score()
        self.assertEqual(resultado, '15 | 0')

    def test_30_0(self):
        """Prueba 30 | 0"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        resultado = self.partido.score()
        self.assertEqual(resultado, '30 | 0')

    def test_40_0(self):
        """Prueba 40 | 0"""
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        self.partido.point_won_by("jugador 1")
        resultado = self.partido.score()
        self.assertEqual(resultado, '40 | 0')

    def test_0_15(self):
        """Prueba 0 | 15"""
        self.partido.point_won_by("jugador 2")
        resultado = self.partido.score()
        self.assertEqual(resultado, '0 | 15')

    def test_0_30(self):
        """Prueba 0 | 30"""
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        resultado = self.partido.score()
        self.assertEqual(resultado, '0 | 30')

    def test_0_40(self):
        """Prueba 0 | 40"""
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        self.partido.point_won_by("jugador 2")
        resultado = self.partido.score()
        self.assertEqual(resultado, '0 | 40')

    def test_jugador_invalido_jugador_3(self):
        """Prueba jugador debe ser 'jugador 1' o 'jugador 2' - jugador 3"""
        resultado = self.partido.point_won_by("jugador 3")
        expected = 'El jugador debe ser "jugador 1" o "jugador 2"'
        self.assertEqual(resultado, expected)

    def test_jugador_invalido_cadena_vacia(self):
        """Prueba jugador - caso cadena vacía"""
        resultado = self.partido.point_won_by("")
        expected = 'El jugador debe ser "jugador 1" o "jugador 2"'
        self.assertEqual(resultado, expected)

    def test_jugador_invalido_numero(self):
        """Prueba jugador debe ser 'jugador 1' o 'jugador 2' - caso número"""
        resultado = self.partido.point_won_by(1)
        expected = ('El jugador debe ser el string "jugador 1" o '
                    '"jugador 2"')
        self.assertEqual(resultado, expected)


if __name__ == '__main__':
    unittest.main()
