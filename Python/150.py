from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                if (a ^ b) < 0:
                    stack.append(-(abs(b) // abs(a)))
                else:
                    stack.append(b // a)
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == "__main__":
    sol = Solution()
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
