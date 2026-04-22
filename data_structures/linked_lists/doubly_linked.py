class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


    def insert(self, idx, element):
        if idx > self.size or idx < 0:
            print(f"You must insert between 0 to {self.size -1}")
            return 
        current = self.head
        i = 0
        while i < idx:
            current = current.next
            i += 1
        next_node = current.next
        new_node = Node(element)
        new_node.next = next_node
        new_node.prev = current
        next_node.prev = new_node
        current.next = new_node
        self.size += 1

    def add(self, element):
        new_node = Node(element)
        last = self.tail.prev

        new_node.prev = last
        new_node.next = self.tail

        last.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def delete(self, idx):
        if idx > self.size or idx < 0:
            print(f"You must insert between 0 to {self.size}")
            return
        current = self.head.next #first real node
        i = 0
        while i < idx:
            current = current.next
            i += 1
        prev_node = current.prev
        next_node = current.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1


    def __repr__(self):
        result = []
        current = self.head
        while current:
            result.append(f"[{current.element}]")
            current = current.next
        return "<->".join(result)
    

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert(0,5)
doubly_linked_list.insert(1,9)
doubly_linked_list.insert(2, 100)
doubly_linked_list.insert(2, 10000)
doubly_linked_list.insert(0, 89)
doubly_linked_list.add(899)
doubly_linked_list.add(89009)
doubly_linked_list.delete(3)

print(doubly_linked_list)
print(doubly_linked_list.size)