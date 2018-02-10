
from node import Node

class LNs(object):
        def __init__(self, dataArg = 'DEFAULT_VALUE'):
                self.__head = Node(dataArg)

        def append(self, data):
                self.__append(self.__head, data)

        def size(self):
                return self.__size(self.__head)

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
                acc = 1
                while nHead.next is not None:
                        acc += 1
                        nHead = nHead.next
                return acc
