class Array:
    """
    Static array implementation.
    """
    def __init__(self, size):
        self.array = [0] * size
        self.length = 0
        self.size = size

    def append(self, val):
        if self.length < self.size:
            self.array[self.length] = val
            self.length += 1
        else:
            print("Error: Array is full.")



    def insert(self, idx, val):
        if self.length <self.size and 0 <= idx <= self.length:
            for i in range(self.length, idx, -1):
                self.array[i] = self.array[i-1]
            self.array[idx] = val
            self.length += 1
        else:
            print("Error: Capacity reached or invalid index.")



    def delete(self, idx):
        if 0 <= idx <= self.length:
            for i in range(idx, self.length-1):
                self.array[i] = self.array[i+1]
            self.array[self.length - 1] = 0
            self.length -= 1
        else:
            print("Error: Invalide index.")


    def update(self, idx, val):
        if idx <= self.length:
            self.array[idx] = val

    def read(self, idx):
        if idx < self.length:
            return self.array[idx]

    def search(self, val):
        for i in range(self.length):
            if self.read(i) == val:
                return i
        return - 1

      
    def __repr__(self):
        return str(self.array[:self.length])
    


array = Array(7)
array.append(2)
array.append(90)
array.append(6)
array.append(3)
array.append(1)
print("=====Array values====")
print(array)
array.insert(2, 300)
print(array)
array.update(3, 1000)
print(array)
array.delete(0)
print(array)
print(array.read(1))
print(array.length)
print(array.search(100))
