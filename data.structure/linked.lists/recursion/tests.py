import unittest
import lns
import fixtures

class lns_api(unittest.TestCase):

    def setUp(self):
        self.lns_instance = lns.linked_nodes()

    def tearDown(self):
        self.lns_instance = None
        
    def test_from_list(self):
        self.lns_instance.from_list(['v1', 'v2', 'v3'])
        self.assertEqual(self.lns_instance.to_list(), ['HEAD', 'v3', 'v2', 'v1', 'END'])

    def test_append(self):
        self.lns_instance.from_list(['v1', 'v2', 'v3'])
        self.lns_instance.append('v4')
        self.assertEqual(self.lns_instance.to_list(), ['HEAD', 'v3', 'v2', 'v1', 'v4', 'END'])

    def test_prepend(self):
        self.lns_instance.from_list(['v1', 'v2', 'v3'])
        self.lns_instance.prepend('v4')
        self.assertEqual(self.lns_instance.to_list(), ['HEAD', 'v4', 'v3', 'v2', 'v1', 'END'])

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(lns_api)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
