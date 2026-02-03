# language: es
Característica: El sistema debe permitir depositar dinero en una cuenta.
    Como cliente
    Quiero depositar dinero en mi cuenta
    Para incrementar mi saldo disponible.

    Escenario: Depositar dinero exitosamente
        Dado que existe el cliente con ID "20" nombre "Roberto Sánchez" registrado
        Y que existe la cuenta con número "2000" para el cliente con ID "20" con saldo de 1000.0
        Cuando deposito 500.0 en la cuenta con número "2000"
        Entonces la cuenta con número "2000" tiene un saldo de 1500.0

    Escenario: Depositar dinero en cuenta con saldo cero
        Dado que existe el cliente con ID "21" nombre "Sofía Ramírez" registrado
        Y que existe la cuenta con número "2100" para el cliente con ID "21" con saldo de 0.0
        Cuando deposito 300.0 en la cuenta con número "2100"
        Entonces la cuenta con número "2100" tiene un saldo de 300.0

    Escenario: Realizar múltiples depósitos
        Dado que existe el cliente con ID "22" nombre "Diego Torres" registrado
        Y que existe la cuenta con número "2200" para el cliente con ID "22" con saldo de 500.0
        Cuando deposito 200.0 en la cuenta con número "2200"
        Y deposito 300.0 en la cuenta con número "2200"
        Entonces la cuenta con número "2200" tiene un saldo de 1000.0
