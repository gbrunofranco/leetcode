class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        temp_min = self.getMin()
        if temp_min is None or val < temp_min:
            temp_min = val

        self.stack.append((val, temp_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2
