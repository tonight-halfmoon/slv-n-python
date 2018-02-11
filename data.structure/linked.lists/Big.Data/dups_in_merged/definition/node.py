import time

class Node(object):
    def __init__(self, dataArg = None, nextArg = None):
        self.__data = dataArg
        self.next = nextArg
        self.__has_been_visited = False
        self.__time_visited = 0

    def ck_data(self):
        return self.__data

    def visit(self):
        self.__has_been_visited = True
        self.__time_visited = time.time()

    def is_visited(self):
        return self.__has_been_visited

    def when_visited(self):
        return self.__time_visited
