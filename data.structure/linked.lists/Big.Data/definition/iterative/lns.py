
from node import Node

class LNs(object):
        def __init__(self, dataArg = 'HEAD'):
                self.__head = Node(dataArg)

        def append(self, data):
                self.__append(self.__head, data)

        def size(self):
                return self.__size(self.__head)

        def from_list(self, listvs = ['v1', 'v2', 'v3']):
                self.__insert_all(self.__head, listvs)

        def __append(self, nHead, data):
                if nHead is None:
                        nHead = Node(data)
                while nHead.next is not None:
                        nHead = nHead.next
                nHead.next = Node(data)

        def __size(self, nHead):
                acc = 0
                if nHead is None:
                        return acc
                while nHead.next is not None:
                        acc += 1
                        nHead = nHead.next
                return acc

        def __insert_all(self, nHead, listvs):
                if listvs is None or len(listvs) is 0:
                        return False
                if nHead is None:
                        nHead = Node(listvs.pop())
                while nHead.next is not None:
                        nHead = nHead.next
                for n in listvs:
                        nHead.next = Node(n)
                        nHead = nHead.next
