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

def mergek_lists(lists):
    if not lists:
        return None
    result = lists[0]
    for i in range(1, len(lists)):
        result = merge_sorted_list(result, lists[i])
    return result