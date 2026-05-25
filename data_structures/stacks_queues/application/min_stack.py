class MinStack:

    def __init__(self):
        self._data = []
        self._min = []
        

    def push(self, val: int) -> None:
        self._data.append(val)
        min_val = min(val, self._min[-1] if self._min else val)
        self._min.append(min_val)

        
    def pop(self) -> None:
        self._data.pop()
        self._min.pop()
        

    def top(self) -> int:
        return self._data[-1]
        

    def getMin(self) -> int:
        return self._min[-1]