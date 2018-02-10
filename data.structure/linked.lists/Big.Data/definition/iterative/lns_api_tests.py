
import unittest
import lns
import fixtures

class LNsAPI_TestCase(unittest.TestCase):
      
      def setUp(self):
            self.lns10K = fixtures.setup_10K_lns()

      def tearDown(self):
            self.lns10K = None

      def test_size(self):
            self.assertEqual(self.lns10K.size(), 10001)
