import unittest
import constants
import json

from coinbase.wallet.client import Client

def connectClient():
    return Client(constants.api_key, constants.api_secret)

# Get Accounts
def getUserAccounts():
    client = connectClient()
    return client.get_accounts()

# Get User Info
def getUserInfo():
    client = connectClient()
    user = client.get_current_user()
    return json.dumps(user)

def buyBitCoin(account_id, amount, currency):
    client = connectClient()
    client.buy(account_id, amount, currency)

def sellBitCoin(account_id, amount, currency):
    client = connectClient()
    client.sell(account_id, amount, currency)

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testConnectClient(self):
        connectClient()

    def testGetUserInfo(self):
        getUserInfo()

def main():
    unittest.main()

if __name__ == '__main__':
    main()
