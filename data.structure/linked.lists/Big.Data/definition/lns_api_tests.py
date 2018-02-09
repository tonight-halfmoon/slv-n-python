import unittest
import lns
import fixtures

class LNsAPI_TestCase(unittest.TestCase):

    def setUp(self):
        self.lns_instance = lns.LNs()

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

    def test_search_must_not_be_found(self):
        self.lns_instance.from_list(['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12'])
        self.assertEqual(self.lns_instance.search('v13'), 'not_found')

    def test_search_must_be_found(self):
        self.lns_instance.from_list(['v1', 'v2', 'v10', 'v90', 'v4', 'v7'])
        self.assertEqual(self.lns_instance.search('v10'), 'found')

    def test_remove_last(self):
        self.lns_instance.from_list(['v2', 'v1', 'v10'])
        self.lns_instance.remove_last()
        self.assertEqual(self.lns_instance.to_list(), ['HEAD', 'v10', 'v1', 'END'])

    def test_remove_fist(self):
        self.lns_instance.from_list(['v1', 'v100', 'v200'])
        self.lns_instance.remove_first()
        self.assertEqual(self.lns_instance.to_list(), ['HEAD', 'v100', 'v1', 'END'])

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(lns_api)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
