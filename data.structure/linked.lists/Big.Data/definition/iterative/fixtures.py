import lns

def setup_1M_lns():
        lns1M = lns.LNs()
        for n in setup_1M_list():
                lns1M.append(n)
        return lns1M

def setup_1M_elems_lns():
        lns1M = lns.LNs()
        listvs = setup_1M_list()
        lns1M.from_list(listvs)
        return lns1M

def setup_1M_list():
        return ['v' + str(i) for i in range(1, 1000001)]

def setup_10K_list():
        return ['v' + str(i) for i in range(1, 10001)]

def setup_19358_list():
         return ['v' + str(i) for i in range(1, 19359)]
 
def setup_4961_list():
        return ['v' + str(i) for i in range(1, 4962)]

def setup_19358_lns():
        lns19358 = lns.LNs()
        listvs = setup_19358_list()
        lns19358.from_list(listvs)
        return lns19358

def setup_4961_lns():
        lns4961 = lns.LNs()
        listvs = setup_4961_list()
        lns4961.from_list(listvs)
        return lns4961

def setup_10K_lns():
        lns10K = lns.LNs()
        listvs = setup_10K_list()
        for n in listvs:
                lns10K.append(n)
        return lns10K
