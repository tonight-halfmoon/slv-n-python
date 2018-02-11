import unittest
import lns
import fixtures

class LNsAPI_TestCase(unittest.TestCase):

    def setUp(self):
        self.lns_instance = lns.LNs()
        self.lns4961 = fixtures.setup_4961_lns()

    def tearDown(self):
        self.lns_instance = None
        self.lns4961 = None
        
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

    def test_must_not_be_a_member(self):
        self.lns_instance.from_list(['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12'])
        self.assertFalse(self.lns_instance.member('v13'))

    def test_must_be_a_member(self):
        self.lns_instance.from_list(['v1', 'v2', 'v10', 'v90', 'v4', 'v7'])
        self.assertTrue(self.lns_instance.member('v10'))

    def test_v98_must_be_a_member_of_4961_elems_LNs(self):
       self.assertTrue(self.lns4961.member('v98'))

    def test_v4962_must_be_a_member_of_4961_elems_LNs(self):
       self.assertFalse(self.lns4961.member('v4962'))

    def test_remove_last(self):
        self.lns_instance.from_list(['v2', 'v1', 'v10'])
        self.lns_instance.remove_last()
        self.assertEqual(self.lns_instance.to_list(), ['HEAD', 'v10', 'v1', 'END'])

    def test_remove_first(self):
        self.lns_instance.from_list(['v1', 'v100', 'v200'])
        self.lns_instance.remove_first()
        self.assertEqual(self.lns_instance.to_list(), ['HEAD', 'v100', 'v1', 'END'])

    def test_size(self):
        self.assertEqual(self.lns4961.size(), 4961)

    def test_from_list_4961(self):
        self.lns_instance = lns.LNs()
        self.lns_instance.from_list(fixtures.setup_4961_list())
        self.assertEqual(self.lns_instance.size(), 4961)

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(lns_api)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
