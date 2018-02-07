"""
  
  Recursion on Linked Lists

  A linked list is a list of linked nodes
 
  @author Ahmad Elghafari 
  @date   February 7th, 2018

"""

import sys

class node(object):
    def __init__(self, dataArg = None, nextArg = None):
        self.data = dataArg
        self.next = nextArg

class linked_nodes(object):
    def __init__(self):
        self.head = Node('HEAD', Node('END'))
        
    def from_list(self, listvs = ['v1', 'v2', 'v3']):
        self.insert_all(self.head, listvs).next = self.head.next

    def append(self, data):
        self.append_internal(self.head, data)

    def prepend(self, data):
        HEAD = self.head
        HEAD.next = self.prepend_internal(self.head.next, data)
        
    def print(self):
        self.print_internal(self.head)

    def search(self, data):
        return self.search_internal(self.head, data)

    def remove_last(self):
        self.remove_last_internal(self.head)

    def remove_all(self):
        HEAD = self.head
        HEAD.next = self.remove_all_internal(self.head)
        
    def insert_all(self, nHead, listvs):
        return self.insert_next(nHead, listvs)

    def insert_next(self, nHead, listvs):
        if len(listvs) is 0:
            return nHead
        nHead.next = node(listvs.pop())
        return self.insert_next(nHead.next, listvs)
        
    def print_internal(self, nHead):
        if nHead is None:
            sys.stdout.write('\n')
            return True
        sys.stdout.write(nHead.data)
        if nHead.next is not None:
            sys.stdout.write(' --> ')
        self.print_internal(nHead.next)

    def search_internal(self, nHead, data):
        if nHead is None:
            return 'not_found'
        if nHead.data is data:
            return 'found'
        return self.search_internal(nHead.next, data)

    def remove_last_internal(self, nHead):
        if nHead.next.next.data is 'END':
            nHead.next = nHead.next.next
            return True
        self.remove_last_internal(nHead.next)

    def append_internal(self, nHead, data):
        if nHead.next.data is 'END':
            tEND = nHead.next
            nHead.next = node(data)
            nHead.next.next = tEND
            return True
        self.append_internal(nHead.next, data)

    def prepend_internal(self, nHead, data):
        if nHead is not None:
            return node(data, nHead)

    def remove_all_internal(self, nHead):
        if nHead.data is 'END':
            return nHead
        return self.remove_all_internal(nHead.next)
    
if __name__ == '__main__':
    ln1 = linked_nodes()
    ln1.print()
    ln1.from_list(['v1', 'v2', 'v3', 'v4'])
    ln1.print()
    print('\'v5\' ' + ln1.search('v5'))
    ln1.append('v5')
    print('\'v4\' ' + ln1.search('v4'))
    ln1.print()
    print('attempt to remove last element')
    ln1.remove_last()
    ln1.print()
    ln1.prepend('v9')
    ln1.print()
    ln1.append('v10')
    ln1.print()
    print('Removing all elements')
    ln1.remove_all()
    ln1.print()
