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

class Node(object):
    def __init__(self, dataArg=None, nextArg=None):
        self.data = dataArg
        self.next = nextArg
        
"""" API """

def show(head1, head2):
    dict_ = {}
    traverse(head1, dict_)
    update_dict(dict_, head2)
    return dict([{k, v} for k, v in dict_.items() if v > 0])

def to_linkedlist(data=['v1', 'v2', 'v3']):
    head = Node(data.pop())
    insert_all(head, data)
    return head

def append(head, data):
    newNode =  Node(data, None)
    if head is None:
        return newNode
    myHead = head
    while myHead.next is not None:
        myHead = myHead.next
    myHead.next = newNode
    return head

def insert_all(head, vs):
    if head is None:
        return None
    insert_next(head, vs, None)

def printme(head):
    if head is None:
        sys.stdout.write('\n')
        return
    sys.stdout.write(head.data)
    if head.next is not None:
        sys.stdout.write(', ')
    printme(head.next)

""" Internal Functions """

def insert_next(nextnode, vs, nextv):
    if len(vs) is 0:
        return nextnode
    nextv = vs.pop()
    insert_next(insert_internal(nextnode, nextv), vs, nextv)

"""
insert_internal(had, data)
@private

Append a node immediately after the provided head. Therefore, it overrides the head.next value if there is any.
Return a pointer to the new node (not to the provided head) 
"""

def insert_internal(head, data):
    newNode =  Node(data, None)
    if head is None:
        return newNode
    head.next = newNode
    return head.next
    
def traverse(head, dict_= {}):
    if head is None:
        return dict_
    if dict_ is None:
        dict_ = {}
    dict_[head.data] = 0
    traverse(head.next, dict_ )

def update_dict(dict_, head):
    if head is None:
        return dict_
    if dict_ is None:
        return head
    if head.data in dict_:
        dict_[head.data] += 1
    update_dict(dict_, head.next)

""" Sample client """
""" @public """

if __name__ == '__main__':
  l1 = Node('v0')
  append(l1, 'v1')
  append(l1, 'v2')
  append(l1, 'v8')
  append(l1, 'v8')
  sys.stdout.write("l1: ")
  printme(l1)

  l2 = Node('v0')
  vs = ['v8', 'v10', 'v2', 'v8']
  insert_all(l2, vs)
  sys.stdout.write("l2: ")
  printme(l2)
  show(l1, l2)

""" Evaluate with  `python dups.py` """
