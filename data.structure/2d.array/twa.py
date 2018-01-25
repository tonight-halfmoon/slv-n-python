# -------------------------------------------------------------------
# @author  <rosemary@SCUBA>
# @copyright (C) 2017, 
# @doc
# Problem Statement
#
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
#
# Sample Output
# 19
#
# @end
#
# In 2015 by  <rosemary@SCUBA>
# -------------------------------------------------------------------
#!/bin/python

import sys

tda = []
for i in xrange(6):
    r = map(int, raw_input().strip().split(' '))
    tda.append(r)

def subsums(tda):
    ss  = list()
    for q in xrange(4):
        for u in xrange(4):
            subsum = 0
            for i in range(q,q+3):
                if ((q+3) % (i+1)) == 1:
                    subsum += tda[i][u+1]
                else:
                    subsum += sum(tda[i][k] for k in xrange(u,u+3))
            ss.append(subsum)
    return ss

print max(subsums(tda))
