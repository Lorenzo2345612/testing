from typing import Dict
class Cliente:
    id: int
    nombre: str

    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

class Cuenta:
    numero: int
    saldo: float
    cliente: Cliente

    def __init__(self, numero: int, saldo: float, cliente: Cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

class CajeroAutomatico:
    clientes: Dict[int, Cliente]
    cuentas: Dict[int, Cuenta]
    contador_clientes: int = 0
    contador_cuentas: int = 0

    def __init__(self):
        self.clientes = {}
        self.cuentas = {}

    def registrar_cliente(self, nombre: str) -> Cliente:
        """Registra un nuevo cliente y devuelve el objeto Cliente."""
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre inválido")

        self.contador_clientes += 1
        cliente = Cliente(self.contador_clientes, nombre)
        self.clientes[cliente.id] = cliente
        return cliente
    
    def registrar_cuenta(self, cliente_id: int, saldo_inicial: float) -> Cuenta:
        """Registra una nueva cuenta para un cliente existente y devuelve el objeto Cuenta."""
        if not isinstance(saldo_inicial, (int, float)) or saldo_inicial < 0:
            raise ValueError("Saldo inicial inválido")
        
        if not isinstance(cliente_id, int) or cliente_id <= 0:
            raise ValueError("ID de cliente inválido")
        
        if cliente_id not in self.clientes:
            raise ValueError("Cliente no registrado")
        
        self.contador_cuentas += 1
        cuenta = Cuenta(self.contador_cuentas, saldo_inicial, self.clientes[cliente_id])
        self.cuentas[cuenta.numero] = cuenta
        return cuenta
    
    def consultar_saldo(self, cuenta_numero: int) -> float:
        """Consulta el saldo de una cuenta existente."""
        if not isinstance(cuenta_numero, int) or cuenta_numero <= 0:
            raise ValueError("Número de cuenta inválido")
        
        if cuenta_numero not in self.cuentas:
            raise ValueError("Cuenta no registrada")
        
        return self.cuentas[cuenta_numero].saldo
    
    def retirar_dinero(self, cuenta_numero: int, monto: float) -> float:
        """Retira dinero de una cuenta existente y devuelve el nuevo saldo."""
        if not isinstance(cuenta_numero, int) or cuenta_numero <= 0:
            raise ValueError("Número de cuenta inválido")
        
        if cuenta_numero not in self.cuentas:
            raise ValueError("Cuenta no registrada")
        
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("Monto inválido")
        
        cuenta = self.cuentas[cuenta_numero]
        if monto > cuenta.saldo:
            raise ValueError("Fondos insuficientes")
        
        cuenta.saldo -= monto
        return cuenta.saldo
    
    def depositar_dinero(self, cuenta_numero: int, monto: float) -> float:
        """Deposita dinero en una cuenta existente y devuelve el nuevo saldo."""
        if not isinstance(cuenta_numero, int) or cuenta_numero <= 0:
            raise ValueError("Número de cuenta inválido")
        
        if cuenta_numero not in self.cuentas:
            raise ValueError("Cuenta no registrada")
        
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("Monto inválido")
        
        cuenta = self.cuentas[cuenta_numero]
        cuenta.saldo += monto
        return cuenta.saldo
    
