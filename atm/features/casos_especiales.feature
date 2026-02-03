# language: es
Característica: El sistema debe manejar casos especiales y validaciones.
    Como sistema de cajero automático
    Quiero validar las operaciones y manejar errores
    Para garantizar la integridad de las transacciones.

    Escenario: Intentar crear cuenta para cliente no registrado
        Cuando intento crear cuenta con número "9000" para el cliente con ID "9999" con saldo inicial de 1000.0
        Entonces obtengo el error "Cliente no registrado"

    Escenario: Intentar consultar saldo de cuenta inexistente
        Cuando intento consultar el saldo de la cuenta con número "9999"
        Entonces obtengo el error "Cuenta no registrada"

    Escenario: Intentar depositar en cuenta inexistente
        Cuando intento depositar 500.0 en la cuenta con número "9999"
        Entonces obtengo el error "Cuenta no registrada"

    Escenario: Intentar retirar de cuenta inexistente
        Cuando intento retirar 500.0 de la cuenta con número "9999"
        Entonces obtengo el error "Cuenta no registrada"

    Escenario: Intentar crear cuenta con saldo negativo
        Dado que existe el cliente con ID "40" nombre "José Ortiz" registrado
        Cuando intento crear cuenta con número "4000" para el cliente con ID "40" con saldo inicial de -100.0
        Entonces obtengo el error "Saldo inicial inválido"

    Escenario: Intentar depositar monto negativo
        Dado que existe el cliente con ID "41" nombre "Carmen Suárez" registrado
        Y que existe la cuenta con número "4100" para el cliente con ID "41" con saldo de 1000.0
        Cuando intento depositar -200.0 en la cuenta con número "4100"
        Entonces obtengo el error "Monto inválido"
        Y la cuenta con número "4100" tiene un saldo de 1000.0

    Escenario: Intentar retirar monto negativo
        Dado que existe el cliente con ID "42" nombre "Andrés Rojas" registrado
        Y que existe la cuenta con número "4200" para el cliente con ID "42" con saldo de 1000.0
        Cuando intento retirar -300.0 de la cuenta con número "4200"
        Entonces obtengo el error "Monto inválido"
        Y la cuenta con número "4200" tiene un saldo de 1000.0

    Escenario: Intentar depositar monto cero
        Dado que existe el cliente con ID "43" nombre "Patricia Vega" registrado
        Y que existe la cuenta con número "4300" para el cliente con ID "43" con saldo de 1000.0
        Cuando intento depositar 0.0 en la cuenta con número "4300"
        Entonces obtengo el error "Monto inválido"
        Y la cuenta con número "4300" tiene un saldo de 1000.0

    Escenario: Intentar retirar monto cero
        Dado que existe el cliente con ID "44" nombre "Ricardo Méndez" registrado
        Y que existe la cuenta con número "4400" para el cliente con ID "44" con saldo de 1000.0
        Cuando intento retirar 0.0 de la cuenta con número "4400"
        Entonces obtengo el error "Monto inválido"
        Y la cuenta con número "4400" tiene un saldo de 1000.0

    Escenario: Operaciones combinadas - depósito y retiro
        Dado que existe el cliente con ID "50" nombre "Verónica Silva" registrado
        Y que existe la cuenta con número "5000" para el cliente con ID "50" con saldo de 1000.0
        Cuando deposito 500.0 en la cuenta con número "5000"
        Y retiro 300.0 de la cuenta con número "5000"
        Y deposito 200.0 en la cuenta con número "5000"
        Entonces la cuenta con número "5000" tiene un saldo de 1400.0

    Escenario: Verificar saldo no cambia después de operación fallida
        Dado que existe el cliente con ID "51" nombre "Tomás Navarro" registrado
        Y que existe la cuenta con número "5100" para el cliente con ID "51" con saldo de 500.0
        Cuando intento retirar 1000.0 de la cuenta con número "5100"
        Entonces obtengo el error "Fondos insuficientes"
        Cuando consulto el saldo de la cuenta con número "5100"
        Entonces obtengo un saldo de 500.0
