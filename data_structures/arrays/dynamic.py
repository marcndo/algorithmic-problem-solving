from typing import Any

class DynamicArray:
    """Implement dynamic array
    """
    def __init__(self, size) -> None:
        self.length = 0
        self.size = size
        self.array = [0] * self.size

    
    def resize_array(self) -> list[Any]:
        if self.length == self.size:
            self.size *= 2
            new_array = [0] * self.size 
            for i in range(self.length):
                new_array[i] = self.array[i]
            self.array = new_array
        return self.array
    
    def insert(self, idx: int,val: Any) -> None:
        if idx < 0 or idx > self.length:
            return "Index out of bound"
        self.resize_array()
        for i in range(self.length, idx, -1):
            self.array[i] = self.array[i-1]
        self.array[idx] = val 
        self.length += 1


    def append(self, val: int|float) -> None:
        self.array = self.resize_array()
        self.array[self.length] = val
        self.length += 1

    def delete(self, idx: int) -> None:
        if idx < 0 or idx > self.length:
            return "Index out of bound"
        for i in range(idx, self.length, -1):
            self.array[i] = self.array[i+1]
        self.array[self.length-1] = 0
        self.length -= 1
        

    def update(self, idx: int, val: int|float) -> None:
        if idx < 0 or idx > self.length:
            return "Index out of bound"
        self.array[idx] = val

    def read(self, idx: int) -> Any:
        if idx < self.length:
            return self.array[idx]
    

    def search(self, val: int) -> bool:
        i = 0
        while i < self.length:
            if self.read(i) == val:
                print(self.read(i))
                return True
            i += 1
        return False


    def __repr__(self) -> str:
        return str(self.array[:self.length])



dynamic_array = DynamicArray(3)
dynamic_array.append(7)
dynamic_array.append(9)
dynamic_array.append(5)
dynamic_array.append(56)
dynamic_array.append(78)
dynamic_array.append(90)
dynamic_array.append(100)
dynamic_array.insert(7, 1)
dynamic_array.insert(8, 30)
dynamic_array.insert(9, 780)
dynamic_array.insert(10, 89)
dynamic_array.delete(0)
dynamic_array.insert(10, 780)
print(dynamic_array.read(7))
print(dynamic_array)
print(dynamic_array.search(56))
