from definition import lns

def setup_lns_with_range(from_, to):
    to +=1
    listvs = ['v' + str(n) for n in range(from_, to)]
    LNs = lns.LNs()
    LNs.from_list(listvs)
    return LNs

def setup_merged_and_extended(lns1, lns2, lns3):
    lns1.tail_merge(lns2)
    lns1.extend(lns3)
    return lns1

def setup_two_merged_LNss_9_elems():
    lns1 = setup_lns_with_range(1, 3)
    lns2 = setup_lns_with_range(4, 5)
    lns3 = setup_lns_with_range(6, 9)
    lns1.tail_merge_with(lns2, lns3)
