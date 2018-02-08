"""
    February 4th 2018

    Problem Statement: find out duplicate nodes in two Big linked lists
    
    Logic assumes both linked lists are completely independent, i.e., each head references different memory and there is no node.next points to a node in a different linked list.

    Duplicate in the first linked list is not considered
    All duplicate instances in the second linked list of a node in the first linked list will be counted

   Development Time:
   Evaluate `. runt_tests.sh` to check results of Unit Tests

   TODO:
    - Performance, Time and Spatial complexity analysis
"""

import sys
from definition import lns

class Show(object):
    
    def show(self, lns1, lns2):
        dict_ = {}
        self.init_dict(lns1, dict_)
        self.update_dict(dict_, lns2)
        return [{k,v} for (k,v) in dict_.items() if v > 0]

    def init_dict(self, lns, dict_= {}):
        if lns is None:
            return dict_
        if dict_ is None:
            dict_ = {}
        return self.__init_dict_next(lns.ck_head(), dict_)

    def __init_dict_next(self, nxt_node, dict_):
        if nxt_node is None:
            return dict_
        dict_[nxt_node.ck_data()] = 0
        return self.__init_dict_next(nxt_node.ck_next(), dict_)

    def update_dict(self, dict_, lns):
        if lns is None:
            return dict_
        if dict_ is None:
            return head
        return self.__update_dict_next(lns.ck_head(), dict_)

    def __update_dict_next(self, nxt_node, dict_):
        if nxt_node is None:
            return dict_
        if nxt_node.ck_data() in dict_:
            dict_[nxt_node.ck_data()] += 1
        return self.__update_dict_next(nxt_node.ck_next(), dict_)

""" Sample client """
""" @public """

if __name__ == '__main__':
  l1 = lns.linked_nodes()
  l1.from_list(['v1', 'v2', 'v3', 'v4', 'v6'])
  l1.print_()
  
  l2 = lns.linked_nodes()
  l2.from_list(['v0', 'v5', 'v3', 'v4', 'v5'])
  print(Show().show(l1, l2))

""" Evaluate with  `python dups.py` """
