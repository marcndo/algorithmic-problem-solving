def reorderList(head):
    if not head or not head.next:
        return

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None 

    # step 2 — reverse second half
    prev = None
    curr = second
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    second = prev

    # step 3 — merge alternately
    first = head
    while second:
        next_first = first.next
        next_second = second.next
        first.next = second
        second.next = next_first
        first = next_first
        second = next_second