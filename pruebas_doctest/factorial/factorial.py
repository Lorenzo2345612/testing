def factorial(n):
    """
    Calcula el factorial de un número entero no negativo n.

    El factorial de un número n (denotado como n!) es el producto de todos los enteros positivos desde 1 hasta n.
    Por definición, el factorial de 0 es 1.

    Parámetros:
    n (int): Un número entero no negativo.

    Retorna:
    int: El factorial de n.

    Raises:
    ValueError: Si n es un número negativo.
    TypeError: Si n no es un entero.
    TypeError: Si n no es un número.
    """
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un entero.")

    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado