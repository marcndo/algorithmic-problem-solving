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
            print(f"You must insert between 0 to {self.size}")
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
        i = 0
        new_node = Node(element)
        current = self.head
        while current is not None and i < self.size:
            current = current.next
            i += 1
        current.next = new_node
        new_node.next = self.tail
        self.size += 1
        

    def delete(self, idx):
        if idx > self.size or idx < 0:
            print(f"You must insert between 0 to {self.size}")
            return
        current = self.head
        i = 1
        while i < idx:
            current = current.next
            i += 1
        print(i)
        current.prev = current.next.next
        current.next = current.prev
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