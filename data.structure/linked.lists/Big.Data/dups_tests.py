import unittest
from dups import Show
import fixtures
from definition import lns

class show_duplicates_test_case(unittest.TestCase):

    def setUp(self):
        self.lns1 = lns.linked_nodes()
        self.lns1.from_list(['v0', 'v2'])
        self.lns2 = lns.linked_nodes()
        self.lns2.from_list(['v0', 'v10', 'v9'])
        self.lns3 = lns.linked_nodes()
        self.lns3.from_list(['s0'])

    def tearDown(self):
        self.lns1 = None
        self.lns2 = None
        self.lns3 = None
        
    def test_when_2nd_linkedlist_has_dups_then_dups_must_be_shown(self):
        self.assertListEqual(Show().play(self.lns1, self.lns2), [('HEAD', 1), ('v0', 1), ('END', 1)])

    def test_when_no_duplicates_then_nothing_to_be_shown(self):
        
        self.assertListEqual(Show().play(self.lns1, self.lns3), [('HEAD', 1), ('END', 1)])

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(show_test_case)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
