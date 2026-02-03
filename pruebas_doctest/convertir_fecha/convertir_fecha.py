from re import fullmatch
from numero_a_letra import numero_a_letra


class ValidadorFecha:
    def __init__(self):
        self.meses_en_letras = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre",
            "diciembre"
        ]

    def validar_formato(self, fecha: str):
        match_fecha = fullmatch(r'([0-3][0-9])/([0-1][0-9])/([0-9]{4})', fecha)
        if not match_fecha:
            raise ValueError("El formato de la fecha debería ser dd/mm/aaaa")
        return map(int, match_fecha.groups())

    def validar_componentes(self, dia: int, mes: int, anyo: int):
        if mes < 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12")

        if anyo < 0:
            raise ValueError("El año debe ser un número positivo")

        if anyo > 3000:
            raise ValueError("El año debe ser menor o igual a 3000")

        dias_por_mes = [31, 29 if anyo % 4 == 0 else 28,
                        31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if dia < 1 or dia > dias_por_mes[mes - 1]:
            raise ValueError(
                f"El día debe estar entre 1 y {dias_por_mes[mes - 1]} "
                f"para el mes {mes}")


def convertir_fecha(fecha: str) -> str:
    """Convierte una fecha del formato "dd/mm/aaaa" al formato de texto.
    Args:
        fecha (str): Fecha en formato "dd/mm/aaaa".
    Returns:
        str: Fecha en formato "dia de mes de aaaa" o error si inválida.
    """
    validador = ValidadorFecha()
    dia, mes, anyo = validador.validar_formato(fecha)
    validador.validar_componentes(dia, mes, anyo)

    dia_en_letras = numero_a_letra(dia)
    anyo_en_letras = numero_a_letra(anyo)
    mes_en_letras = validador.meses_en_letras[mes - 1]
    return f"{dia_en_letras} de {mes_en_letras} de {anyo_en_letras}"
