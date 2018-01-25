"""
 Check if linked list has a cycle
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return 0 if no cycle else return 1
"""

def HasCycle(head):

    if head == None:
        return 0
        
    d = 0
    newD = 0
    tourtle = head
    rabit = head
    
    while rabit.next != None:    
        newD = move(tourtle, rabit, d)
        if newD - d <= 0:
            return 1
        else:
            d = newD
     
    return 0
            
def move(t, r, d):
    t = t.next
    if r.next == None or r.next.next == None:
        return d-1
    
    r = r.next.next
    
    i=0
    sanjoob = t
    while sanjoob != r:
        sanjoob = sanjoob.next
        i = i + 1
          
    return i
