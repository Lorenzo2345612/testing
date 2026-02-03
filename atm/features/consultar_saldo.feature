# language: es
Característica: El sistema debe permitir consultar el saldo de una cuenta.
    Como cliente
    Quiero consultar el saldo de mi cuenta
    Para saber cuánto dinero tengo disponible.

    Escenario: Consultar saldo de cuenta existente
        Dado que existe el cliente con ID "10" nombre "Ana Martínez" registrado
        Y que existe la cuenta con número "1000" para el cliente con ID "10" con saldo de 2500.0
        Cuando consulto el saldo de la cuenta con número "1000"
        Entonces obtengo un saldo de 2500.0

    Escenario: Consultar saldo después de crear cuenta
        Dado que existe el cliente con ID "11" nombre "Carlos Ruiz" registrado
        Cuando creo una cuenta con número "1100" para el cliente con ID "11" con saldo inicial de 750.0
        Y consulto el saldo de la cuenta con número "1100"
        Entonces obtengo un saldo de 750.0

    Escenario: Consultar saldo de cuenta con saldo cero
        Dado que existe el cliente con ID "12" nombre "Laura Fernández" registrado
        Y que existe la cuenta con número "1200" para el cliente con ID "12" con saldo de 0.0
        Cuando consulto el saldo de la cuenta con número "1200"
        Entonces obtengo un saldo de 0.0
