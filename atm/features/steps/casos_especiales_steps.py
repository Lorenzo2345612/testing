from behave import given, when, then
from cajero_automatico import Cliente, Cuenta, CajeroAutomatico

@when(u'intento crear cuenta con número "{numero_cuenta}" para el cliente con ID "{id_cliente}" con saldo inicial de {saldo_inicial:f}')
def step_impl(context, numero_cuenta, id_cliente, saldo_inicial):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    try:
        context.cajero.registrar_cuenta(int(id_cliente), saldo_inicial)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@when(u'intento consultar el saldo de la cuenta con número "{numero_cuenta}"')
def step_impl(context, numero_cuenta):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    try:
        context.saldo_consultado = context.cajero.consultar_saldo(int(numero_cuenta))
        context.error = None
    except ValueError as e:
        context.error = str(e)

@when(u'intento depositar {monto:f} en la cuenta con número "{numero_cuenta}"')
def step_impl(context, monto, numero_cuenta):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    try:
        context.cajero.depositar_dinero(int(numero_cuenta), monto)
        context.error = None
    except ValueError as e:
        context.error = str(e)
