from behave import *

@given(u'A time in space')
def step_impl(context):
    from time import time
    time()

@when('ComputeLiteCoinBuySignal is called')
def step_imp(context):
    from cryptoTSAnalysis import getLitecoinBuySignal
    from time import time
    getLitecoinBuySignal(time())

@then(u'An ExecutionSignal will be returned')
def step_impl(context):
    import executionsignal
    executionsignal.BuySignal.BUY
