
def intersection(headA, headB):
    seenA = set()
    current = headA
    while current:
        seenA.add(current):
        current = current.next
    current = headB
    while current:
        if current in seenA:
            return current
        else:
            current = current.next
    return None
    
