from behave import given, when, then
from cajero_automatico import Cliente, Cuenta, CajeroAutomatico

@given(u'que existe el cliente con ID "{id_cliente}" nombre "{nombre}" registrado')
def step_impl(context, id_cliente, nombre):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    cliente = Cliente(int(id_cliente), nombre)
    context.cajero.clientes[int(id_cliente)] = cliente

@when(u'creo una cuenta con número "{numero_cuenta}" para el cliente con ID "{id_cliente}" con saldo inicial de {saldo_inicial:f}')
def step_impl(context, numero_cuenta, id_cliente, saldo_inicial):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    cuenta = Cuenta(int(numero_cuenta), saldo_inicial, context.cajero.clientes[int(id_cliente)])
    context.cajero.cuentas[int(numero_cuenta)] = cuenta

@then(u'la cuenta con número "{numero_cuenta}" tiene un saldo de {saldo_esperado:f}')
def step_impl(context, numero_cuenta, saldo_esperado):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    saldo_actual = context.cajero.cuentas[int(numero_cuenta)].saldo
    assert saldo_actual == saldo_esperado, \
        f'Se esperaba un saldo de {saldo_esperado} y se obtuvo {saldo_actual}.'
