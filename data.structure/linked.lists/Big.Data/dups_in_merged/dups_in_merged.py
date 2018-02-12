"""
    February 4th 2018

    Problem Statement: find out duplicate nodes in two Big linked lists
    
    Implemented Logic assumes that each provided linked list starts with a unique head but then they do merge at some node later. 

    The merged two linked lists continue as one linked list.

    [*] Unit Testing and Development Time:
       - Evaluate `. runt_tests.sh` to check results of Unit Tests

    [*] TODO:
       - Performance, Time and Spatial complexity analysis
   
"""

from definition import lns

class DupsInTwoMergedLNsChecker(object):
        
        def find_duplicates(self, LNs1, LNs2):
                dict_ = {}
                if LNs1 is None:
                        return dict_
                nxtNode = LNs1.ck_head()
                while nxtNode is not None:
                        nxtNode.visit()
                        dict_[nxtNode.ck_data()] = 0
                        nxtNode = nxtNode.ck_next()
                if LNs2 is None:
                        return dict_
                nxtNode = LNs2.first()
                while nxtNode is not None:
                        if nxtNode.ck_data() in dict_ and nxtNode.is_visited() == False:
                                dict_[nxtNode.ck_data()] += 1
                        nxtNode = nxtNode.ck_next()
                return [(k,v) for (k,v) in dict_.items() if v > 0]
