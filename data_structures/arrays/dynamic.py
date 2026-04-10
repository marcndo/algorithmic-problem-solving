from typing import Any

class DynamicArray:
    """Implement dynamic array
    """
    def __init__(self, size) -> None:
        self.length = 0
        self.size = size
        self.array = [0] * self.size

    
    def resize_array(self) -> Any:
        if self.length == self.size:
            self.array = self.array + [0] * self.length
            self.size = self.length + self.size - 1
        return self.array
    
    def insert(self, idx: int,val: Any) -> None:
        self.array = self.resize_array()
        temp = self.array[idx]
        self.array[idx] = val
        while idx < self.size - 1:
            next_val = self.array[idx + 1]
            self.array[idx + 1] = temp
            temp = next_val
            idx += 1
        self.length += 1


    def append(self, val: int|float) -> None:
        self.array = self.resize_array()
        self.array[self.length] = val
        self.length += 1

    def delete(self, idx: int) -> None:
        while idx < self.size:
            next_val = self.array[idx + 1]
            self.array[idx] = next_val
            idx += 1
        

    def update(self, idx: int, val: int|float) -> None:
        self.array[idx] = val

    def read(self, idx: int):
        return self.array[idx]

    def search(self, idx) -> bool:
        for i in range(self.length):
            if self.read(i) == self.read(idx):
                print(self.read(i))
                return True
            return False

    def __repr__(self) -> str:
        return str(self.array)



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
dynamic_array.insert(11, 600)
print(dynamic_array.read(7))
print(dynamic_array)
