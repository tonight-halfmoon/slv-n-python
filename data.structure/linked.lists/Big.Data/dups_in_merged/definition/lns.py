"""
  
  Recursion on Linked Lists

  A linked list is a list of linked nodes
 
  @author Ahmad Elghafari 
  @date   February 7th, 2018

"""

from node import Node
import sys
sys.setrecursionlimit(5000)

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

    def member(self, data):
        return self.__is_element(self.__head, data)

    def remove_last(self):
        self.__remove_last(self.__head)

    def remove_all(self):
        HEAD = self.__head
        HEAD.next = self.__remove_all(self.__head)

    def remove_first(self):
        Head = self.__head
        Head.next = Head.next.next

    def size(self):
        return self.__size(self.__head, -2)

    def ck_node_data(self):
        return self.__ck_node_data(self.__head)

    def ck_next_node(self):
        return self.__ck_next_node(self.__head)

    def ck_head(self):
        return self.__head

    def tail_merge(self, LNs):
        Head = self.__head
        if Head is None:
            return {}
        if LNs is None:
            return Head
        LNsHead = LNs.ck_head()
        if LNsHead is None:
            return Head
        endSelf = self.end()
        tailLNs = LNs.tail()
        tailLNs.next = endSelf
        return True

    def tail(self):
        Head = self.__head
        return self.__tail(Head, Head.next)
        
    def end(self):
        Head = self.__head
        return self.__end(Head, Head.next)

    def tail_merge_with(self, LNsY, LNsF):
        Head = self.__head
        if Head is None:
            return {}
        if LNsY is None:
            return Head
        if LNsF is None:
            return Head
        tailSelf = self.tail()
        tailLNsY = LNsY.tail()
        tailSelf.next = LNsF.first()
        tailLNsY.next = LNsF.first()
        return True

    def first(self):
        Head = self.__head
        if Head is None:
            return {}
        return Head.next
    
    def head(self):
        return self.__head

    def extend(self, LNs):
        Head = self.__head
        if Head is None:
            return {}
        LNsHead = LNs.head()
        if LNsHead is None:
            return Head
        tailSelf = self.tail()
        tailSelf.next = LNsHead

    def visit_all(self):
        self.__visit_all(self.__head)

    def visited(self):
        return self.__visited(self.__head, [])

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

    def __is_element(self, nHead, data):
        if nHead is None:
            return False
        if nHead.ck_data() == data:
            return True
        return self.__is_element(nHead.next, data)

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

    def __size(self, nHead, acc):
        if nHead is None:
            return acc
        acc += 1
        return self.__size(nHead.next, acc)

    def __ck_node_data(self, nHead):
        if nHead is None:
            return {}
        return nHead.ck_data()

    def __ck_next_node(self, nHead):
        if nHead is None:
            return {}
        return nHead.next

    def __end(self, nHead, nNext):
        if nHead is None:
            return {}
        if nNext is None:
            return nHead
        return self.__end(nNext, nNext.next)
        
    def __tail(self, nHead, nNext):
        if nHead is None:
            return {}
        if nNext is None:
            return nHead
        if nNext.ck_data() == 'END':
            return nHead
        return self.__tail(nNext, nNext.next)

    def __visit_all(self, nHead):
        if nHead is None:
            return {}
        if nHead.ck_data() != 'END' and nHead.ck_data() != 'HEAD':
            nHead.visit()
        return self.__visit_all(nHead.next)

    def __visited(self, nHead, VList):
        if nHead is None:
            return VList
        if nHead.is_visited() is True:
            VList.append(nHead.ck_data() + ' at ' + str(nHead.when_visited()))
        return self.__visited(nHead.next, VList)
