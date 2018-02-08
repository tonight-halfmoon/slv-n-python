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
from recursion import lns

def show(head1, head2):
    dict_ = {}
    init_dict_with(head1, dict_)
    update_dict(dict_, head2)
    return dict([{k,v} for k, v in dict_.items() if v > 0])
    
def init_dict_with(head, dict_= {}):
    if head is None:
        return dict_
    if dict_ is None:
        dict_ = {}
    return __init_dict_next_node(head.ck_head(), dict_)

def __init_dict_next_node(next_node, dict_):
    if next_node is None:
        return dict_
    dict_[next_node.ck_data()] = 0
    return __init_dict_next_node(next_node.ck_next(), dict_)

def update_dict(dict_, head):
    if head is None:
        return dict_
    if dict_ is None:
        return head
    return __update_dict_with(head.ck_head(), dict_)

def __update_dict_with(next_node, dict_):
    if next_node is None:
        return dict_
    if next_node.ck_data() in dict_:
        dict_[next_node.ck_data()] += 1
    return __update_dict_with(next_node.ck_next(), dict_)

""" Sample client """
""" @public """

if __name__ == '__main__':
  l1 = lns.linked_nodes()
  l1.from_list(['v1', 'v2', 'v3'])
  l1.print_()
  
  l2 = lns.linked_nodes()
  l2.from_list(['v0', 'v5', 'v3'])
  print(show(l1, l2))

""" Evaluate with  `python dups.py` """
