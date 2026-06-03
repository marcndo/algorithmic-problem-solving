def deleteMiddle(head):
    if not head or not head.next:
        return None

    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next