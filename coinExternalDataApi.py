import unittest

def fetchData():
    return "To Be Implemented"

# Here's our "unit tests".
class functionTests(unittest.TestCase):

    def testFetchData(self):
        print(fetchData())

def main():
    unittest.main()

if __name__ == '__main__':
    main()