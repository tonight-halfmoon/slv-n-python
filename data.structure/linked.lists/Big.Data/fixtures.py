
from definition import lns
import sys
sys.setrecursionlimit(50000)

class fixture(object):

        def setup_1M_list(self):
                return ['v' + str(i) for i in range(1000000)]

        def setup_1M__elems_lns(self):
                listvs = self.setup_1M_list()
                lns1M = lns.LNs()
                lns1M.from_list(listvs)
                return lns1M

        def setup_1M_elems_lns_combinator(self):
                lns1M = lns.LNs()
                for n in self.setup_1M_list():
                        lns1M.append(n)
                return lns1M
        
        def setup_19358_list(self):
                return ['v' + str(i) for i in range(19358)]

        def setup_19358_lns(self):
                listvs = self.setup_19358_list()
                lns19358 = lns.LNs()
                lns19358.from_list(listvs)
                return lns19358

        def lns_2(self):
                lns2 = lns.LNs()
                lns2.from_list(['v0', 'v10', 'v9'])
                return lns2

        def lns_1(self):
                lns1 = lns.LNs()
                lns1.from_list(['v0', 'v2'])
                return lns1

        def lns_3(self):
                lns3 = lns.LNs()
                lns3.from_list(['s0'])
                return lns3
