class ConvertirNumeroALetra:
    def __init__(self):
        self.base = {
            0: 'cero',
            1: 'uno',
            2: 'dos',
            3: 'tres',
            4: 'cuatro',
            5: 'cinco',
            6: 'seis',
            7: 'siete',
            8: 'ocho',
            9: 'nueve',
            10: 'diez',
            11: 'once',
            12: 'doce',
            13: 'trece',
            14: 'catorce',
            15: 'quince',
            16: 'dieciséis',
            17: 'diecisiete',
            18: 'dieciocho',
            19: 'diecinueve',
            20: 'veinte',
            21: 'veintiuno',
            22: 'veintidós',
            23: 'veintitrés',
            24: 'veinticuatro',
            25: 'veinticinco',
            26: 'veintiséis',
            27: 'veintisiete',
            28: 'veintiocho',
            29: 'veintinueve',
            30: 'treinta',
            40: 'cuarenta',
            50: 'cincuenta',
            60: 'sesenta',
            70: 'setenta',
            80: 'ochenta',
            90: 'noventa',
            100: 'cien',
            200: 'doscientos',
            300: 'trescientos',
            400: 'cuatrocientos',
            500: 'quinientos',
            600: 'seiscientos',
            700: 'setecientos',
            800: 'ochocientos',
            900: 'novecientos',
        }

    def ajustar_un(self, txt: str):
        if txt.endswith('veintiuno'):
            return txt.replace('veintiuno', 'veintiún')
        if txt.endswith(' y uno'):
            return txt.replace(' y uno', ' y un')
        if txt.endswith(' uno'):
            return txt.replace(' uno', ' un')
        if txt == 'uno':
            return 'un'
        return txt

    def _convertir_decenas(self, n):
        d = (n // 10) * 10
        r = n % 10
        if r == 0:
            return self.base[d]
        return self.base[d] + ' y ' + self.base[r]

    def _convertir_centenas(self, n):
        if n == 100:
            return 'cien'
        c = (n // 100) * 100
        r = n % 100
        pref = 'ciento' if c == 100 else self.base[c]
        if r == 0:
            return pref
        return pref + ' ' + self.convertir(r)

    def _convertir_miles(self, n):
        q = n // 1000
        r = n % 1000
        if q == 1:
            pref = 'mil'
        else:
            pref = self.ajustar_un(self.convertir(q)) + ' mil'
        if r == 0:
            return pref
        return pref + ' ' + self.convertir(r)

    def _convertir_millones(self, n):
        q = n // 1000000
        r = n % 1000000
        if q == 1:
            pref = 'un millón'
        else:
            pref = self.ajustar_un(self.convertir(q)) + ' millones'
        if r == 0:
            return pref
        return pref + ' ' + self.convertir(r)

    def convertir(self, n):
        if n == 1000000000:
            return 'mil millones'

        ranges = [
            (30, lambda x: self.base[x]),
            (100, self._convertir_decenas),
            (1000, self._convertir_centenas),
            (1000000, self._convertir_miles),
            (1000000000, self._convertir_millones)
        ]

        for limit, method in ranges:
            if n < limit:
                return method(n)
        return ''

    def _validar_entrada(self, num):
        s = self._convertir_a_string(num)
        if s is None:
            return None, 'Error: Entrada inválida'

        error = self._validar_string_basico(s)
        if error:
            return None, error

        return s, None

    def _convertir_a_string(self, num):
        try:
            s = str(num).strip()
            return s if s else None
        except Exception:
            return None

    def _validar_string_basico(self, s):
        if s[0] == '-':
            return 'Error: Número fuera de rango'

        if self._es_formato_invalido(s):
            return 'Error: Entrada inválida'

        return None

    def _es_formato_invalido(self, s):
        return (s.count('.') > 1 or s == '.' or
                any(ch not in '0123456789.' for ch in s))

    def _procesar_partes(self, s):
        partes = s.split('.') if '.' in s else [s]
        entero_str = partes[0] if partes[0] != '' else '0'
        dec_str = partes[1] if len(partes) > 1 else ''

        try:
            entero = int(entero_str)
        except Exception:
            return None, None, 'Error: Entrada inválida'

        centavos = self._calcular_centavos(dec_str)
        if centavos is None:
            return None, None, 'Error: Entrada inválida'

        return entero, centavos, None

    def _calcular_centavos(self, dec_str):
        if not dec_str:
            return 0
        solo = ''.join(ch for ch in dec_str if ch.isdigit())
        if len(solo) == 1:
            return int(solo) * 10
        elif len(solo) == 2:
            return int(solo)
        return None

    def _validar_rango(self, entero, centavos):
        return not (entero > 1000000000 or
                    (entero == 1000000000 and centavos > 0))

    def _generar_texto_entero(self, entero, centavos):
        if entero == 1 and centavos > 0:
            return 'un'
        if entero == 0:
            return 'cero'
        return self.convertir(entero)

    def _generar_texto_final(self, entero_txt, centavos):
        if centavos > 0:
            cents_txt = self.ajustar_un(self.convertir(centavos))
            suf = 'centavo' if centavos == 1 else 'centavos'
            return entero_txt + ' con ' + cents_txt + ' ' + suf
        return entero_txt

    def numero_a_letra(self, num):
        s, error = self._validar_entrada(num)
        if error:
            return error

        entero, centavos, error = self._procesar_partes(s)
        if error:
            return error

        if not self._validar_rango(entero, centavos):
            return 'Error: Número fuera de rango'

        if entero == 0 and centavos == 0:
            return 'cero'

        entero_txt = self._generar_texto_entero(entero, centavos)
        return self._generar_texto_final(entero_txt, centavos)


def numero_a_letra(num):
    converter = ConvertirNumeroALetra()
    return converter.numero_a_letra(num)
