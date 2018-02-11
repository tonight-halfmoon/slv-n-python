from definition import lns

def setup_two_merged_LNss_9_elems():
    lns1 = setup_lns_with_range(1, 3)
    lns2 = setup_lns_with_range(4, 5)
    lns3 = setup_lns_with_range(6, 9)
    lnssMerged = merge(lns1, lns2, lns3)
    return lnssMerged

def setup_lns_with_range(from, to):
    to +=1
    listvs = [for n in range(from, to)]
    lns = lns.LNs()
    lns.from_list(listvs)
    return lns

def merge(lns1, lns2, lns3):
    lns1.tail_merge(lns2)
    lns1.extend(lns3)
    return lns1

"""
    extend(lns1, lns3)
    extend(lns2, lns3)
    return lns1

"""
