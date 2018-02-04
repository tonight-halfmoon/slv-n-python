import unittest
import dups
import fixtures

class show_test_case(unittest.TestCase):

    def setUp(self):
        ll1 = dups.Node('v0')
        dups.append(ll1, 'v2')
        self.head1 = ll1
        ll2 = dups.Node('v0')
        dups.insert_all(ll2, ['v10', 'v9'])
        self.head2 = ll2

    def tearDown(self):
        self.head1 = None
        self.head2 = None
        
    def test_when_2nd_linkedlist_has_dups_then_dups_must_be_shown(self):
        self.assertDictEqual(dups.show(self.head1, self.head2), dict([{'v0', 1}]))

if __name__ == '__main__':
    unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(show_test_case)
unittest.TextTestRunner(verbosity=2).run(suite)
