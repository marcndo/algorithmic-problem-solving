class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    

    def is_empty(self):
        return self.size == 0


    def __len__(self):
        return self.size


    def add_first(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
        current.next = new_node
        self.size += 1

    def insert(self, element, idx):
        if idx == 0:
            self.add_first(element)
            return 
        current = self.head
        count = 1
        while current.next is not None and count < idx:
            current = current.next
            count += 1
        new_node = Node(element)
        new_node.next = current.next 
        current.next = new_node
        self.size += 1

    def delete_first(self):
        if not self.head:
            return
        self.head = self.head.next
        self.size -= 1

    def delete(self, idx):
        if not self.head:
            return 
        elif idx == 0:
            self.head = self.head.next
            self.size -= 1
            return 
        trav1 = self.head
        trav2 = self.head.next
        i = 1
        while trav2 is not None and i < idx:
            trav1 = trav2
            trav2 = trav2.next
            i += 1

        if trav2 is not None:
            trav1.next = trav2.next
        self.size -= 1


    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(f"[{current.element}]")
            current = current.next
        return "-> ".join(nodes)
    
linked_list = SinglyLinkedList()
linked_list.add_first(8)
linked_list.add_first(67)
linked_list.add_first(0)
linked_list.add_first(9)
linked_list.add_last(6)
linked_list.add_last(800)
linked_list.insert(10, 2)
linked_list.delete_first()
linked_list.delete(3)
print(linked_list)




