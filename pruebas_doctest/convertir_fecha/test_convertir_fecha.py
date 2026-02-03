
import unittest
from convertir_fecha import convertir_fecha

"""
Único formato de fecha aceptado: dd/mm/aaaa
Día: 2 dígitos
Mes: 2 dígitos
Año: 4 dígitos
"""


class TestConvertirFecha(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Iniciando tests de convertir_fecha")

    @classmethod
    def tearDownClass(cls):
        print("\nFinalizando tests de convertir_fecha")

    def test_fecha_valida(self):
        """Probando con una fecha válida"""
        resultado = convertir_fecha("05/10/2023")
        self.assertEqual(resultado, "cinco de octubre de dos mil veintitrés")

    def test_veintiuno(self):
        """Probando con una fecha con día 21"""
        resultado = convertir_fecha("21/03/2023")
        self.assertEqual(resultado, "veintiuno de marzo de dos mil veintitrés")

    def test_fecha_dia_uno(self):
        """Probando con una fecha con día 1"""
        resultado = convertir_fecha("01/01/2023")
        self.assertEqual(resultado, "uno de enero de dos mil veintitrés")

    def test_fecha_mes_dos_digitos(self):
        """Probando con una fecha con mes de dos dígitos"""
        resultado = convertir_fecha("15/11/2023")
        self.assertEqual(
            resultado, "quince de noviembre de dos mil veintitrés")

    def test_fecha_mes_un_digito(self):
        """Probando con una fecha con mes de un dígito"""
        resultado = convertir_fecha("15/04/2023")
        self.assertEqual(resultado, "quince de abril de dos mil veintitrés")

    def test_fecha_formato_incorrecto(self):
        """Probando con una fecha en formato incorrecto"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("2023/10/05")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_fecha_dia_fuera_rango(self):
        """Probando con una fecha con día fuera de rango"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("32/10/2023")
        self.assertEqual(str(cm.exception),
                         "El día debe estar entre 1 y 31 para el mes 10")

    def test_fecha_mes_fuera_rango(self):
        """Probando con una fecha con mes fuera de rango"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("15/13/2023")
        self.assertEqual(str(cm.exception), "El mes debe estar entre 1 y 12")

    def test_fecha_anyo_incorrecto(self):
        """Probando con una fecha con año incorrecto"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("15/10/23")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_fecha_no_numerica(self):
        """Probando con una fecha no numérica"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("dd/mm/aaaa")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_29_febrero_año_bisiesto(self):
        """Probando con una fecha 29 de febrero en un año bisiesto"""
        resultado = convertir_fecha("29/02/2020")
        self.assertEqual(resultado, "veintinueve de febrero de dos mil veinte")

    def test_29_febrero_año_no_bisiesto(self):
        """Probando con una fecha 29 de febrero en un año no bisiesto"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("29/02/2021")
        self.assertEqual(str(cm.exception),
                         "El día debe estar entre 1 y 28 para el mes 2")

    def test_año_mayor_3000(self):
        """Probando con una fecha con año mayor a 3000"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("15/10/3001")
        self.assertEqual(str(cm.exception),
                         "El año debe ser menor o igual a 3000")

    def test_año_negativo(self):
        """Probando con una fecha con año negativo"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("15/10/-2023")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_fecha_vacia(self):
        """Probando con una fecha vacía"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_fecha_texto(self):
        """Probando con una fecha que es solo texto"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("fecha inválida")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_fecha_espacios(self):
        """Probando con una fecha con espacios"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha(" 15 / 10 / 2023 ")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_fecha_caracteres_especiales(self):
        """Probando con una fecha con caracteres especiales"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("15-10-2023")
        self.assertEqual(str(cm.exception),
                         "El formato de la fecha debería ser dd/mm/aaaa")

    def test_fecha_en_cero(self):
        """Probando con una fecha con día y mes en cero"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("00/00/2023")
        self.assertEqual(str(cm.exception), "El mes debe estar entre 1 y 12")

    def test_fecha_dia_31_mes_abril(self):
        """Probando con una fecha con día 31 en abril (mes con 30 días)"""
        with self.assertRaises(ValueError) as cm:
            convertir_fecha("31/04/2023")
        self.assertEqual(str(cm.exception),
                         "El día debe estar entre 1 y 30 para el mes 4")
