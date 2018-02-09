import sys
From definition import lns

class DupsIn2LNsRecursive(object):
    def play(self, lns1, lns2):
        dict_ = {}
        self.init_dict(lns1, dict_)
        self.update_dict(dict_, lns2)
        return [(k,v) for (k,v) in dict_.items() if v > 0]

    def init_dict(self, lns, dict_= {}):
        if lns is None:
            return dict_
        if dict_ is None:
            dict_ = {}
        return self.__init_dict_next(lns.ck_head(), dict_)

    def __init_dict_next(self, nxt_node, dict_):
        if nxt_node is None:
            return dict_
        dict_[nxt_node.ck_data()] = 0
        return self.__init_dict_next(nxt_node.ck_next(), dict_)

    def update_dict(self, dict_, lns):
        if lns is None:
            return dict_
        if dict_ is None:
            return head
        return self.__update_dict_next(lns.ck_head(), dict_)

    def __update_dict_next(self, nxt_node, dict_):
        if nxt_node is None:
            return dict_
        if nxt_node.ck_data() in dict_:
            dict_[nxt_node.ck_data()] += 1
        return self.__update_dict_next(nxt_node.ck_next(), dict_)
