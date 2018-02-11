from node import Node
import sys

class LNs(object):
        def __init__(self, dataArg = 'HEAD'):
                self.__head = Node(dataArg)

        def append(self, data):
                self.__append(self.__head, data)

        def size(self):
                return self.__size(self.__head)

        def from_list(self, listvs = ['v1', 'v2', 'v3']):
                self.__insert_all(self.__head, listvs)

        def print_(self):
                self.__print(self.__head)

        def member(self, data):
                return True

        def remove_last(self):
                print('TODO: not implemented')
                None

        def prepend(self, data):
                print('TODO: not implemented')
                None

        def remove_first(self):
                print('TODO: not implemented')
                None

        def remove_all(self):
                print('TODO: not implemented')
                None

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
                if nHead is None:
                        nHead = Node(listvs.pop())
                while nHead.next is not None:
                        nHead = nHead.next
                for n in listvs:
                        nHead.next = Node(str(n))
                        nHead = nHead.next

        def __print(self, nHead):
                if nHead is None:
                        sys.stdout.write('EMPTY LINKED NODE')
                sys.stdout.write('\n')
                while nHead.next is not None:
                        sys.stdout.write(nHead.ck_data())
                        sys.stdout.write(' --> ')
                        nHead = nHead.next
                sys.stdout.write(nHead.ck_data())
                sys.stdout.write('\n')
