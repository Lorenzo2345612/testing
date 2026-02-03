from behave import given, when, then
from cajero_automatico import CajeroAutomatico

@when(u'retiro {monto:f} de la cuenta con número "{numero_cuenta}"')
def step_impl(context, monto, numero_cuenta):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    context.cajero.retirar_dinero(int(numero_cuenta), monto)

@when(u'intento retirar {monto:f} de la cuenta con número "{numero_cuenta}"')
def step_impl(context, monto, numero_cuenta):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    try:
        context.cajero.retirar_dinero(int(numero_cuenta), monto)
        context.error = None
    except ValueError as e:
        context.error = str(e)

@then(u'obtengo el error "{mensaje_error}"')
def step_impl(context, mensaje_error):
    assert context.error == mensaje_error, \
        f'Se esperaba el error "{mensaje_error}" y se obtuvo "{context.error}".'
