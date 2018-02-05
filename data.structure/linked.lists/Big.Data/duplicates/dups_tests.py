import unittest
import dups
import fixtures

class show_test_case(unittest.TestCase):

    def setUp(self):
        self.head1 = dups.to_linkedlist(['v0', 'v2'])
        self.head2 = dups.to_linkedlist(['v0', 'v10', 'v9'])
        self.head3 = dups.Node('s0')

    def tearDown(self):
        self.head1 = None
        self.head2 = None
        self.head3 = None
        self.head33 = None
        self.head332 = None
        
    def test_when_2nd_linkedlist_has_dups_then_dups_must_be_shown(self):
        self.assertDictEqual(dups.show(self.head1, self.head2), dict([{1, 'v0'}]))

    def test_when_no_duplicates_then_nothing_to_be_shown(self):
        self.assertDictEqual(dups.show(self.head1, self.head3), dict({}))

if __name__ == '__main__':
    unittest.main()

"""
suite = unittest.TestLoader().loadTestsFromTestCase(show_test_case)
unittest.TextTestRunner(verbosity=2).run(suite)
"""
