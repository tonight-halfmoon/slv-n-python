""" Sample client """
""" @public """

from dups import DupsInTwoLNsChecker
from definition import lns

if __name__ == '__main__':
  l1 = lns.LNs()
  l1.from_list(['v1', 'v2', 'v3', 'v4', 'v6'])
  l1.print_()
  
  l2 = lns.LNs()
  l2.from_list(['v0', 'v5', 'v3', 'v4', 'v5'])
  print(DupsInTwoLNsChecker().find_duplicates(l1, l2))

""" Evaluate with  `python dups_client.py` """
