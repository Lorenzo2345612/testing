# language: es
Característica: El sistema debe permitir retirar dinero de una cuenta.
    Como cliente
    Quiero retirar dinero de mi cuenta
    Para disponer de efectivo cuando lo necesite.

    Escenario: Retirar dinero exitosamente
        Dado que existe el cliente con ID "30" nombre "Elena Castro" registrado
        Y que existe la cuenta con número "3000" para el cliente con ID "30" con saldo de 1000.0
        Cuando retiro 400.0 de la cuenta con número "3000"
        Entonces la cuenta con número "3000" tiene un saldo de 600.0

    Escenario: Retirar todo el saldo disponible
        Dado que existe el cliente con ID "31" nombre "Fernando Vargas" registrado
        Y que existe la cuenta con número "3100" para el cliente con ID "31" con saldo de 500.0
        Cuando retiro 500.0 de la cuenta con número "3100"
        Entonces la cuenta con número "3100" tiene un saldo de 0.0

    Escenario: Realizar múltiples retiros
        Dado que existe el cliente con ID "32" nombre "Gabriela Morales" registrado
        Y que existe la cuenta con número "3200" para el cliente con ID "32" con saldo de 1500.0
        Cuando retiro 300.0 de la cuenta con número "3200"
        Y retiro 200.0 de la cuenta con número "3200"
        Entonces la cuenta con número "3200" tiene un saldo de 1000.0

    Escenario: Intentar retirar más dinero del disponible
        Dado que existe el cliente con ID "33" nombre "Hugo Delgado" registrado
        Y que existe la cuenta con número "3300" para el cliente con ID "33" con saldo de 500.0
        Cuando intento retirar 800.0 de la cuenta con número "3300"
        Entonces obtengo el error "Fondos insuficientes"
        Y la cuenta con número "3300" tiene un saldo de 500.0

    Escenario: Intentar retirar de cuenta con saldo cero
        Dado que existe el cliente con ID "34" nombre "Isabel Herrera" registrado
        Y que existe la cuenta con número "3400" para el cliente con ID "34" con saldo de 0.0
        Cuando intento retirar 100.0 de la cuenta con número "3400"
        Entonces obtengo el error "Fondos insuficientes"
        Y la cuenta con número "3400" tiene un saldo de 0.0
