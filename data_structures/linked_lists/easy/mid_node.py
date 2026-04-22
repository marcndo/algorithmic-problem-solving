"Given the head of a linked list return the mid node"


head = [1,2,3,4,5]
def mid_node(head):
    size = len(head)
    current = head
    i = 0
    mid = size // 2
    while i <= mid:
        #current = current.next
        i += 1
    return head[i]

print(mid_node([1,2,3,4,5]))
