def oddEvenList(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
    
    odd  = head
    even = head.next
    even_head = even      
    
    while even and even.next:
        odd.next = even.next      
        odd = head.next     
        even.next = odd.next
        even = even.next  
    odd.next = even_head     
    return head