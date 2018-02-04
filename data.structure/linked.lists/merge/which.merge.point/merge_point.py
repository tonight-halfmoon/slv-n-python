
""" 
   Problem Statement: Find out the node at which both lists merge and return the data of that node

[Linked-List #1] a --> b --> c
                              \
                               x --> y --> z --> END
                              /
     [Linked-List #2] p --> q
"""

class Node(object):
    def __init__(self, dataArg=None, nextArg=None):
        self.data = dataArg
        self.next = nextArg

def which(head1, head2):
    while head1 is not None:
        t2 = head2
        while t2 is not None:
            if t2 != head1:
                t2 = t2.next
            else:
                return head1.data
        head1 = head1.next
