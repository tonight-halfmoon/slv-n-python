"""
  
  Recursion on Linked Lists

  A linked list is a list of linked nodes
 
  @author Ahmad Elghafari 
  @date   February 7th, 2018

"""

import sys
sys.setrecursionlimit(5000)

class Node(object):
    def __init__(self, dataArg = None, nextArg = None):
        self.__data = dataArg
        self.next = nextArg

    def ck_data(self):
        return self.__data

    def ck_next(self):
        return self.next

class LNs(object):
    def __init__(self):
        self.__head = Node('HEAD', Node('END'))
        
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
        return self.__seek(self.__head, data)

    def remove_last(self):
        self.__remove_last(self.__head)

    def remove_all(self):
        HEAD = self.__head
        HEAD.next = self.__remove_all(self.__head)

    def remove_first(self):
        Head = self.__head
        Head.next = Head.next.next

    def ck_node_data(self):
        return self.__ck_node_data(self.__head)

    def ck_next_node(self):
        return self.__ck_next_node(self.__head)

    def ck_head(self):
        return self.__head
        
    def __insert_all(self, nHead, listvs):
        return self.__insert_next(nHead, listvs)

    def __insert_next(self, nHead, listvs):
        if len(listvs) is 0:
            return nHead
        nHead.next = Node(listvs.pop())
        return self.__insert_next(nHead.next, listvs)
        
    def __print(self, nHead):
        if nHead is None:
            sys.stdout.write('\n')
            return True
        sys.stdout.write(nHead.ck_data())
        if nHead.next is not None:
            sys.stdout.write(' --> ')
        self.__print(nHead.next)

    def __seek(self, nHead, data):
        if nHead is None:
            return 'not_found'
        if nHead.ck_data() == data:
            return 'found'
        return self.__seek(nHead.next, data)

    def __remove_last(self, nHead):
        if nHead is None:
            return False
        if nHead.next is not None and nHead.next.next is not None and nHead.next.next.ck_data() is 'END':
            nHead.next = nHead.next.next
            return True
        self.__remove_last(nHead.next)

    def __append(self, nHead, data):
        if nHead is None:
            return False
        if nHead.next is not None and nHead.next.ck_data() is 'END':
            tEND = nHead.next
            nHead.next = Node(data, tEND)
            return True
        self.__append(nHead.next, data)

    def __prepend(self, nHead, data):
        if nHead is not None:
            return Node(data, nHead)

    def __remove_all(self, nHead):
        if nHead is None:
            return False
        if nHead.ck_data() is 'END':
            return nHead
        return self.__remove_all(nHead.next)

    def __to_list(self, nHead, listvs):
        if nHead is None:
            return listvs
        listvs.append(nHead.ck_data())
        return self.__to_list(nHead.next, listvs)

    def __ck_node_data(self, nHead):
        if nHead is None:
            return {}
        return nHead.ck_data()

    def __ck_next_node(self, nHead):
        if nHead is None:
            return {}
        return nHead.ck_next()
