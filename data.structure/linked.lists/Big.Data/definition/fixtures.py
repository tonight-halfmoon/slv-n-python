import lns

def setup_LNs1():
        lns1 = lns.LNs()
        lns1.from_list(['v1', 'v2', 'v3', 'v4', 'v5'])      
        return lns1

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
