import unittest
from dups import DupsInTwoLNsChecker
import fixtures
from definition import lns

class DupsInTwoLNsCheckerTestCase(unittest.TestCase):

    def setUp(self):
        fxt = fixtures.fixture()
        self.lns1 = fxt.lns_1()
        self.lns2 = fxt.lns_2()
        self.lns3 = fxt.lns_3()
        self.lns19358 = fxt.setup_19358_lns()

    def tearDown(self):
        self.lns1 = None
        self.lns2 = None
        self.lns3 = None
        self.lns19358 = []

    def test_when_two_linked_lists_having_19358_nodes_identical_must_pass(self):
        self.assertEqual(len(DupsInTwoLNsChecker().find_duplicates(self.lns19358, self.lns19358)), 19360) 
        
    def test_when_2nd_linkedlist_has_dups_then_dups_must_be_shown(self):
        self.assertListEqual(DupsInTwoLNsChecker().find_duplicates(self.lns1, self.lns2), [('HEAD', 1), ('v0', 1), ('END', 1)])

    def test_when_no_duplicates_then_nothing_to_be_shown(self):
        
        self.assertListEqual(DupsInTwoLNsChecker().find_duplicates(self.lns1, self.lns3), [('HEAD', 1), ('END', 1)])

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(DupsInTwoLNsCheckerTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
