class Calculadora:
    def sumar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Sólo se aceptan números'
        if a < 0 or b < 0:
            return 'Sólo se pueden sumar números positivos'
        if not isinstance(a, int) or not isinstance(b, int):
            return 'Sólo se pueden sumar números enteros'
        return a + b

    def restar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Sólo se aceptan números'
        if a < 0 or b < 0:
            return 'Sólo se pueden restar números positivos'
        if not isinstance(a, int) or not isinstance(b, int):
            return 'Sólo se pueden restar números enteros'
        return a - b
    
    def multiplicar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Sólo se aceptan números'
        if a < 0 or b < 0:
            return 'Sólo se pueden multiplicar números positivos'
        if not isinstance(a, int) or not isinstance(b, int):
            return 'Sólo se pueden multiplicar números enteros'
        return a * b
    
    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Sólo se aceptan números'
        if a < 0 or b < 0:
            return 'Sólo se pueden dividir números positivos'
        if not isinstance(a, int) or not isinstance(b, int):
            return 'Sólo se pueden dividir números enteros'
        if b == 0:
            return 'No se puede dividir entre cero'
        return a / b
    
    def potencia(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Sólo se aceptan números'
        if a < 0 or b < 0:
            return 'Sólo se pueden elevar a potencia números positivos'
        if not isinstance(a, int) or not isinstance(b, int):
            return 'Sólo se pueden elevar a potencia números enteros'
        return a ** b
    
    def raiz(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return 'Sólo se aceptan números'
        if a < 0 or b <= 0:
            return 'Sólo se pueden calcular raíces de números positivos'
        if not isinstance(a, int) or not isinstance(b, int):
            return 'Sólo se pueden calcular raíces de números enteros'
        return a ** (1 / b)
    


        
        