class MinStack:
    data = []
    min = []

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.min) > 0:
            self.min.append(min(self.getMin(), val))
        else:
            self.min.append(val)

        self.data.append(val)

    def pop(self) -> None:
        self.min.pop()
        return self.data.pop()

    def top(self) -> int:
        el = self.data.pop()
        self.data.append(el)
        return el

    def getMin(self) -> int:
        if len(self.min) > 0:
            el = self.min.pop()
            self.min.append(el)
            return el

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()