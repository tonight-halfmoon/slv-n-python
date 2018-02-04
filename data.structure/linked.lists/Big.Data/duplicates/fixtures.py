import dups

def setup_ll1():
        ll1 = dups.Node('v0')
        dups.append(ll1, 'v2')
        dups.printme(ll1)
        return ll1

def setup_ll2():
        ll2 = dups.Node('v1')
        dups.insert_all(ll2, ['v10', 'v9'])
        return ll2
