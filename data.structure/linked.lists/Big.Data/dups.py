"""
    February 4th 2018

    Problem Statement: find out duplicate nodes in two Big linked lists
    
    Implemented Logic assumes both linked lists are completely independent, i.e., each head references different memory and there is no node.next points to a node in a different linked list.

    Duplicate instances in the first linked list is not considered
    All duplicate instances in the second linked list of a node in the first linked list will be counted

    [*] Unit Testing and Development Time:
       - Evaluate `. runt_tests.sh` to check results of Unit Tests

    [*] TODO:
       - Performance, Time and Spatial complexity analysis
"""

import sys
from definition import lns

class DupsInTwoLNsChecker(object):
    
    def find_duplicates(self, lns1, lns2):
        dict_ = {}
        if lns1 is None:
            return dict_
        nxtNode = lns1.ck_head()
        while nxtNode is not None:
            dict_[nxtNode.ck_data()] = 0
            nxtNode = nxtNode.ck_next()
        if lns2 is None:
            return dict_
        nxtNode = lns2.ck_head()
        while nxtNode is not None:
            if nxtNode.ck_data() in dict_:
                dict_[nxtNode.ck_data()] += 1
            nxtNode = nxtNode.ck_next()
        return [(k,v) for (k,v) in dict_.items() if v > 0]

""" Sample client """
""" @public """

if __name__ == '__main__':
  l1 = lns.LNs()
  l1.from_list(['v1', 'v2', 'v3', 'v4', 'v6'])
  l1.print_()
  
  l2 = lns.LNs()
  l2.from_list(['v0', 'v5', 'v3', 'v4', 'v5'])
  print(DupsInTwoLNsChecker().find_duplicates(l1, l2))

""" Evaluate with  `python dups.py` """
