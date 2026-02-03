from behave import given, when, then
from cajero_automatico import CajeroAutomatico

@when(u'deposito {monto:f} en la cuenta con número "{numero_cuenta}"')
def step_impl(context, monto, numero_cuenta):
    if not hasattr(context, 'cajero'):
        context.cajero = CajeroAutomatico()
    context.cajero.depositar_dinero(int(numero_cuenta), monto)
