"https://leetcode.com/problems/insertion-sort-list/description/"
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

def insertion(head):
    dummy = Node(0, head)
    prev, current = head, head.next
    while current:
        if prev.val < current.val:
            prev, current = current, current.next
            continue
        temp = dummpy
        while curren.val >= temp.next.val:
            temp = temp.next
        prev.next = current.next
        current.next = temp.next
        temp.next = current
        current = prev.next
    return dummpy.next




