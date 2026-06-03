
def merge_sorted_list(head1, head2):
    dummy = Node(0)
    tail = dummy # tracks where to add node
    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    tail.next = head1 if head1 else head2
    return dummy.next