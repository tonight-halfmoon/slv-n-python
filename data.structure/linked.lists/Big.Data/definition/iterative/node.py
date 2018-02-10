
class Node(object):
    def __init__(self, dataArg = None, nextArg = None):
        self.__data = dataArg
        self.next = nextArg

    def ck_data(self):
        return self.__data

    def ck_next(self):
        return self.next
