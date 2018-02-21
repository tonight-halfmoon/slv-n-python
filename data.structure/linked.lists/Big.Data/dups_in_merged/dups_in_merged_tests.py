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

    def test_when_empty_lns1_provided_then_no_computation_to_perform_and_that_yield_in_empty_tuple(self):
        LNs1 = lns.LNs()
        LNs2 = fixtures.setup_lns_with_range(1, 5)
        LNs1.tail_merge_with(LNs2, lns.LNs())
        self.assertEqual(DupsInTwoMergedLNsChecker().find_duplicates(LNs1, LNs2), {})

    def test_when_empty_lns2_provided_then_no_computation_to_perform_and_that_yield_in_empty_tuple(self):
        LNs1 = fixtures.setup_lns_with_range(1, 5)
        LNs2 = lns.LNs()
        LNs1.tail_merge_with(LNs2, lns.LNs())
        self.assertEqual(DupsInTwoMergedLNsChecker().find_duplicates(LNs1, LNs2), {})

    def test_when_all_duplicates_in_the_second_linked_list_are_considered(self):
        LNs1 = lns.LNs()
        LNs1.from_list(['v1', 'v2', 'v9', 'v28'])
        LNs2 = lns.LNs()
        LNs2.from_list(['v1', 'v1', 'v2', 'v2', 'v2'])
        LNs1.tail_merge_with(LNs2, lns.LNs())
        self.assertListEqual(DupsInTwoMergedLNsChecker().find_duplicates(LNs1, LNs2), [('v2', 3), ('v1', 2)])

    def test_when_any_duplicate_in_the_first_linked_list_is_not_considered(self):
        LNs1 = lns.LNs()
        LNs1.from_list(['v1', 'v1', 'v2', 'v2', 'v2'])
        LNs2 = lns.LNs()
        LNs2.from_list(['v9', 'v28'])
        LNs1.tail_merge_with(LNs2, lns.LNs())
        self.assertListEqual(DupsInTwoMergedLNsChecker().find_duplicates(LNs1, LNs2), [])

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(DupsInTwoMergedLNsTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
