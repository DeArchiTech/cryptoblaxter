import unittest
import constants
from coinbase.wallet.client import Client

def fetchData():
    return "To Be Implemented"

def connectClient():
    return Client(constants.api_key, constants.api_secret)

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testFetchData(self):
        print(fetchData())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
