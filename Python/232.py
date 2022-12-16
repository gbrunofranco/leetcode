class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move_to_out_stack()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move_to_out_stack()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move_to_out_stack(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


if __name__ == "__main__":
    queue = MyQueue()
    assert queue.empty() == True
    assert queue.push(1) is None
    assert queue.push(2) is None
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() == False
    assert queue.pop() == 2
    assert queue.empty() == True
