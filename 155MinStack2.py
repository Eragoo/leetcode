class MinStack:
    data = []
    min = []

    def __init__(self):
        self.min = []
        self.data = []

    def push(self, val: int) -> None:
        if len(self.min) > 0:
            self.min.append(min(self.getMin(), val))
        else:
            self.min.append(val)
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.min.pop()

    def top(self) -> int:
        a = self.data.pop()
        self.data.append(a)
        return a

    def getMin(self) -> int:
        if len(self.min) > 0:
            pop = self.min.pop()
            self.min.append(pop)
            return pop
