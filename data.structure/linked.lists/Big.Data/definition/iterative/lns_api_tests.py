
import unittest
import lns
import fixtures

class LNsAPI_TestCase(unittest.TestCase):

      def setUp(self):
            self.lns_instance = lns.LNs()
            self.lns10K = fixtures.setup_10K_lns()

      def tearDown(self):
            self.lns_instance = None
            self.lns10K = None

      def test_size(self):
            self.assertEqual(self.lns10K.size(), 10000)

      def test_from_list_4961(self):
        self.lns_instance.from_list(fixtures.setup_4961_list())
        self.assertEqual(self.lns_instance.size(), 4961)
