from google.appengine.ext import testbed
import unittest

class MainTestClass(unittest.TestCase):
    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()

    def tearDown(self):
        self.testbed.deactivate()

    # @unittest.skip('See if its active')
    # def test_is_active(self):
    #     self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()