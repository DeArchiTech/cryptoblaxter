import executionsignal

def getEthereiumBuySignal(time):
    return executionsignal.BuySignal.BUY

def getLitecoinBuySignal(time):
    return executionsignal.BuySignal.SELL
