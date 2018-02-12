import unittest
from dups_in_merged import DupsInTwoMergedLNsChecker
import fixtures
from definition import lns

class DupsInTwoMergedLNsTestCase(unittest.TestCase):

    def setUp(self):
        None
    def tearDown(self):
        None

    def test_dups_in_merged_no_dups(self):
        LNs1 = fixtures.setup_lns_with_range(1, 5)
        LNs2 = fixtures.setup_lns_with_range(6, 7)
        LNs3 = fixtures.setup_lns_with_range(8, 9)
        LNs1.tail_merge_with(LNs2, LNs3)
        self.assertListEqual(DupsInTwoMergedLNsChecker().find_duplicates(LNs1, LNs2), [])

    def test_dups_in_merge_has_two_dups(self):
        LNs1 = fixtures.setup_lns_with_range(1, 5)
        LNs2 = fixtures.setup_lns_with_range(1, 2)
        LNs3 = fixtures.setup_lns_with_range(6, 10)
        LNs1.tail_merge_with(LNs2, LNs3)
        self.assertListEqual(DupsInTwoMergedLNsChecker().find_duplicates(LNs1, LNs2), [('v2',1), ('v1', 1)])

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(DupsInTwoMergedLNsTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
