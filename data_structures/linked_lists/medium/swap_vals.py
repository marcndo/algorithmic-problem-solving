def swapNodes(head, k):
    fast = head
    slow = head

    for _ in range(k - 1):
        fast = fast.next
    front = fast
    
    while fast.next:
        fast = fast.next
        slow = slow.next

    front.val, slow.val = slow.val, front.val

    return head