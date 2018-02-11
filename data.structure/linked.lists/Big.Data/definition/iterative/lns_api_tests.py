
import unittest
import lns
import fixtures

class LNsAPI_TestCase(unittest.TestCase):

      def setUp(self):
            self.lns4961 = lns.LNs()
            self.lns10K = fixtures.setup_10K_lns()
            self.list4961 = fixtures.setup_4961_list()

      def tearDown(self):
            self.lns4961 = None
            self.lns10K = None
            self.list4961 = []

      def test_size(self):
            self.assertEqual(self.lns10K.size(), 10000)

      def test_from_list_4961(self):
        self.lns4961.from_list(self.list4961)
        self.assertEqual(self.lns4961.size(), 4961)

      def test_to_list_4961(self):
            self.lns4961.from_list(self.list4961)
            self.assertListEqual(self.lns4961.to_list(), self.list4961)
