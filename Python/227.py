class Solution:
    def calculate(self, s: str) -> int:
        def update(operation, value):
            if operation == "+":
                stack.append(value)
            elif operation == "-":
                stack.append(-value)
            elif operation == "*":
                stack.append(stack.pop() * value)
            elif operation == "/":
                stack.append(int(stack.pop() / value))

        iteration, number, stack, operation = 0, 0, [], "+"

        while iteration < len(s):
            if s[iteration].isdigit():  # there is another digit -> we need to update the number
                number = number*10 + int(s[iteration])
            elif s[iteration] in "+-*/":
                # the first number of the first operation "doesn't matter", we simply put it in the stack
                update(operation, number)
                number, operation = 0, s[iteration]
            iteration += 1
        update(operation, number)

        return sum(stack)


if __name__ == "__main__":
    ex = Solution()

    assert ex.calculate("3+2*2") == 7
    assert ex.calculate("3/2") == 1
    assert ex.calculate("3+5 / 2") == 5
