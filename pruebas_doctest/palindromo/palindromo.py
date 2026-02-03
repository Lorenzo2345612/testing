'''
Primera ejecución

---

1 items had failures:
7 of 7 in palindromo.es_palindromo
**_Test Failed_** 7 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Código mínimo para la primera prueba

def es_palindromo(cadena: str):
    l = 0
    r = len(cadena) - 1
    while l < r:
        while l < r and not cadena[l].isalpha():
            l += 1
        while l < r and not cadena[r].isalpha():
            r -= 1
        if cadena[l] == cadena[r]:
            return False
        l += 1
        r -= 1
    return True

Resultado

---

File "C:\Universidad\Testing\pruebas_doctest\calculadora\palindromo.py", line 43, in palindromo.es_palindromo
Failed example:
es_palindromo("Anita lava la tina")
Expected:
True
Got:
False

---

File "C:\Universidad\Testing\pruebas_doctest\calculadora\palindromo.py", line 45, in palindromo.es_palindromo
Failed example:
es_palindromo("A mamá Roma le aviva el amor a mamá")
Expected:
True
Got:
False

---

File "C:\Universidad\Testing\pruebas_doctest\calculadora\palindromo.py", line 49, in palindromo.es_palindromo
Failed example:
es_palindromo("No 'X' in Nixon")
Expected:
True
Got:
False

---

1 items had failures:
3 of 7 in palindromo.es_palindromo
**_Test Failed_** 3 failures.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Código minimo para la segunda prueba
def es_palindromo(cadena: str):
    l = 0
    r = len(cadena) - 1
    while l < r:
        while l < r and not cadena[l].isalpha():
            l += 1
        while l < r and not cadena[r].isalpha():
            r -= 1
        if cadena[l].lower() != cadena[r].lower():
            return False
        l += 1
        r -= 1
    return True

Resultado:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\blort\AppData\Local\Programs\Python\Python311\Lib\doctest.py", line 2832, in <module>
    sys.exit(_test())
             ^^^^^^^
  File "C:\Users\blort\AppData\Local\Programs\Python\Python311\Lib\doctest.py", line 2820, in _test
    m = __import__(filename[:-3])
        ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Universidad\Testing\pruebas_doctest\calculadora\palindromo.py", line 87
    """
       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 706-707: truncated \UXXXXXXXX escape

Failed example:
    es_palindromo("A mamá Roma le aviva el amor a mamá")
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   7 in palindromo.es_palindromo
***Test Failed*** 1 failures.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Código mínimo para la tercera prueba

def es_palindromo(cadena: str):
    def replace_diacritics(char: str):
        char = (char.lower()
        .replace('á', 'a')
        .replace('ó', 'o')
        .replace('é', 'e')
        .replace('í', 'i')
        .replace('ú', 'u'))
        return char

    l = 0
    r = len(cadena) - 1
    while l < r:
        while l < r and not cadena[l].isalpha():
            l += 1
        while l < r and not cadena[r].isalpha():
            r -= 1
        if replace_diacritics(cadena[l]) != replace_diacritics(cadena[r]):
            return False
        l += 1
        r -= 1
    return True

Resultado:

ok
1 items had no tests:
    palindromo
1 items passed all tests:
   7 tests in palindromo.es_palindromo
7 tests in 2 items.
7 passed and 0 failed.
Test passed.

'''

def es_palindromo(cadena: str):
    """
    Determina si una cadena es un palíndromo, ignorando mayúsculas, espacios y acentos.


    >>> es_palindromo("Anita lava la tina")
    True
    >>> es_palindromo("A mamá Roma le aviva el amor a mamá")
    True
    >>> es_palindromo("Hola mundo")
    False
    >>> es_palindromo("No 'X' in Nixon")
    True
    >>> es_palindromo("Ánita lava la tiña")
    False
    >>> es_palindromo("")
    True
    >>> es_palindromo("A")
    True
    """
    def replace_diacritics(char: str):
        char = (char.lower()
        .replace('á', 'a')
        .replace('ó', 'o')
        .replace('é', 'e')
        .replace('í', 'i')
        .replace('ú', 'u'))
        return char

    l = 0
    r = len(cadena) - 1
    while l < r:
        while l < r and not cadena[l].isalpha():
            l += 1
        while l < r and not cadena[r].isalpha():
            r -= 1
        if replace_diacritics(cadena[l]) != replace_diacritics(cadena[r]):
            return False
        l += 1
        r -= 1
    return True