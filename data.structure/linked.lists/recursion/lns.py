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
        self.__head = node('HEAD', node('END'))
        
    def from_list(self, listvs = ['v1', 'v2', 'v3']):
        self.__insert_all(self.__head, listvs).next = self.__head.next

    def to_list(self):
        return self.__to_list(self.__head, [])
        
    def append(self, data):
        self.__append(self.__head, data)

    def prepend(self, data):
        HEAD = self.__head
        HEAD.next = self.__prepend(self.__head.next, data)
        
    def print_(self):
        self.__print(self.__head)

    def search(self, data):
        return self.__search(self.__head, data)

    def remove_last(self):
        self.__remove_last(self.__head)

    def remove_all(self):
        HEAD = self.__head
        HEAD.__next = self.__remove_all(self.__head)

    def remove_first(self):
        Head = self.__head
        Head.next = Head.next.next
        
    def __insert_all(self, nHead, listvs):
        return self.__insert_next(nHead, listvs)

    def __insert_next(self, nHead, listvs):
        if len(listvs) is 0:
            return nHead
        nHead.next = node(listvs.pop())
        return self.__insert_next(nHead.next, listvs)
        
    def __print(self, nHead):
        if nHead is None:
            sys.stdout.write('\n')
            return True
        sys.stdout.write(nHead.data)
        if nHead.next is not None:
            sys.stdout.write(' --> ')
        self.__print(nHead.next)

    def __search(self, nHead, data):
        if nHead is None:
            return 'not_found'
        if nHead.data is data:
            return 'found'
        return self.__search(nHead.next, data)

    def __remove_last(self, nHead):
        if nHead is None:
            return False
        if nHead.next is not None and nHead.next.next is not None and nHead.next.next.data is 'END':
            nHead.next = nHead.next.next
            return True
        self.__remove_last(nHead.next)

    def __append(self, nHead, data):
        if nHead is None:
            return False
        if nHead.next is not None and nHead.next.data is 'END':
            tEND = nHead.next
            nHead.next = node(data, tEND)
            return True
        self.__append(nHead.next, data)

    def __prepend(self, nHead, data):
        if nHead is not None:
            return node(data, nHead)

    def __remove_all(self, nHead):
        if nHead is None:
            return False
        if nHead.data is 'END':
            return nHead
        return self.__remove_all(nHead.next)

    def __to_list(self, nHead, listvs):
        if nHead is None:
            return listvs
        listvs.append(nHead.data)
        return self.__to_list(nHead.next, listvs)
    
if __name__ == '__main__':
    ln1 = linked_nodes()
    ln1.print_()
    ln1.from_list(['v1', 'v2', 'v3', 'v4'])
    ln1.print_()
    print('\'v5\' ' + ln1.search('v5'))
    ln1.append('v5')
    print('\'v4\' ' + ln1.search('v4'))
    ln1.print_()
    print('attempt to remove last element')
    ln1.remove_last()
    ln1.print_()
    ln1.prepend('v9')
    ln1.print_()
    ln1.append('v10')
    ln1.print_()
    ln1.remove_first()
    ln1.print_()
    print('Removing all elements')
    ln1.remove_all()
    ln1.print_()
