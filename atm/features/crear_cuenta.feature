# language: es
Característica: El sistema debe permitir crear cuentas con saldo inicial.
    Como cliente
    Quiero crear una cuenta con saldo inicial
    Para poder utilizar los servicios del cajero automático.

    Escenario: Crear cuenta con saldo inicial exitosamente
        Dado que existe el cliente con ID "1" nombre "Juan Pérez" registrado
        Cuando creo una cuenta con número "100" para el cliente con ID "1" con saldo inicial de 1000.0
        Entonces la cuenta con número "100" tiene un saldo de 1000.0

    Escenario: Crear cuenta con saldo inicial de cero
        Dado que existe el cliente con ID "2" nombre "María García" registrado
        Cuando creo una cuenta con número "200" para el cliente con ID "2" con saldo inicial de 0.0
        Entonces la cuenta con número "200" tiene un saldo de 0.0

    Escenario: Crear múltiples cuentas para el mismo cliente
        Dado que existe el cliente con ID "3" nombre "Pedro López" registrado
        Cuando creo una cuenta con número "300" para el cliente con ID "3" con saldo inicial de 500.0
        Y creo una cuenta con número "301" para el cliente con ID "3" con saldo inicial de 1500.0
        Entonces la cuenta con número "300" tiene un saldo de 500.0
        Y la cuenta con número "301" tiene un saldo de 1500.0
