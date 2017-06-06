from behave import *

@given('A time in spaces')
def step_imp(context):
    from time import time
    time()

@when('ComputeEthereiumBuySignal Is Called')
def step_impl(context):
    from cryptoTSAnalysis import getEthereiumBuySignal
    from time import time
    getEthereiumBuySignal(time())

@then('An execution Signal will be returned')
def step_impl(context):
    import executionsignal
    executionsignal.BuySignal.BUY
