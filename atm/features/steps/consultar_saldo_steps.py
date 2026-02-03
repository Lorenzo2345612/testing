from behave import given, when, then
from cajero_automatico import Cliente, Cuenta, CajeroAutomatico

@given(u'que existe la cuenta con número "{numero_cuenta}" para el cliente con ID "{id_cliente}" con saldo de {saldo:f}')
def step_impl(context, numero_cuenta, id_cliente, saldo):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    cuenta = Cuenta(int(numero_cuenta), saldo, context.cajero.clientes[int(id_cliente)])
    context.cajero.cuentas[int(numero_cuenta)] = cuenta

@when(u'consulto el saldo de la cuenta con número "{numero_cuenta}"')
def step_impl(context, numero_cuenta):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    context.saldo_consultado = context.cajero.consultar_saldo(int(numero_cuenta))

@then(u'obtengo un saldo de {saldo_esperado:f}')
def step_impl(context, saldo_esperado):
    assert context.saldo_consultado == saldo_esperado, \
        f'Se esperaba un saldo de {saldo_esperado} y se obtuvo {context.saldo_consultado}.'
