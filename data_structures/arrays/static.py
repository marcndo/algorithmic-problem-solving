class Array:
    """
    Static array implementation.
    """
    def __init__(self, size):
        self.array = [0] * size
        self.length = 0
        self.size = size

    def append(self, val):
        self.array[self.length] = val
        self.length += 1

    def insert(self, idx, val):
        if idx <= self.length:
            temp = self.array[idx]
            self.array[idx] = val
            while idx < self.length - 1:
                next_val = self.array[idx+1]
                self.array[idx+1] = temp
                temp = next_val
                idx += 1
        self.length += 1


    def delete(self, idx):
        while idx < self.length - 1:
            next_val = self.array[idx+1]
            self.array[idx] = next_val
            idx += 1
        self.length -= 1

    def update(self, idx, val):
        if idx <= self.length:
            self.array[idx] = val

    def read(self, idx):
        if idx <= self.length:
            return self.array[idx]

    def search(self, val):
        for i in range(self.length):
            print(self.read(i))
            if self.read(i) == val:
                print(self.array[i])
                return True
            return - 1

    def __repr__(self):
        return str(self.array)
    

if "__name__" == "main":
    array = Array(7)
    array.append(2)
    array.append(90)
    array.append(6)
    array.append(3)
    array.append(1)
    print("=====Array values====")
    #print(array)
    array.insert(2, 300)
    #print("====after inserting 300 at position 2")
    array.update(3, 1000)
    array.delete(0)
    print(array.read(1))
    print(array.search(3))
    