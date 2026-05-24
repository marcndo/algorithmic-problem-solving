class Empty(Exception):
    "Error when attempting to access an element inside an empty container"
    pass

class Stack:
    def __init__(self):
        "Creates and empty stack"
        self._data = []
    
    def __len__(self):
        "Returns the number of element in a stack"
        return len(self._data)

    def is_empty(self):
        "Check if a stack is empty"
        return len(self._data) == 0

    def __str__(self):
        "Formats stack display when printed"
        data = []
        for val in self._data:
            data.append(val)
        return str(data)
    
    def push(self, elem):
        "Adds new element to the stack"
        self._data.append(elem)
    
    def pop(self):
        "Removes the last element in the stack"
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        "Displays the last inserted element in a stack"
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]