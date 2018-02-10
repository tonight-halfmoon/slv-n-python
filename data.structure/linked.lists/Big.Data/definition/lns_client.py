from lns import LNs

if __name__ == '__main__':
    ln1 = LNs()
    ln1.print_()
    ln1.from_list(['v1', 'v2', 'v3', 'v4'])
    ln1.print_()
    print('\'v5\' ' + ln1.search('v5'))
    ln1.append('v5')
    print('\'v4\' ' + ln1.search('v4'))
    ln1.print_()
    print('attempt to remove last element')
    ln1.remove_last()
    ln1.print_()
    ln1.prepend('v9')
    ln1.print_()
    ln1.append('v10')
    ln1.print_()
    ln1.remove_first()
    ln1.print_()
    print('Removing all elements')
    ln1.remove_all()
    ln1.print_()
    lns4032 = LNs()
    list4032 = ['v'+ str(n) for n in range(4032)]
    lns4032.from_list(list4032)
    lns4032.print_()
    print(lns4032.search('v134'))
    
