from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)

        stack, ans = deque(), [0]*N

        for idx in range(N-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[idx]:
                stack.pop()
            if len(stack) != 0:
                ans[idx] = stack[-1] - idx
            stack.append(idx)

        return ans


if __name__ == "__main__":
    ex = Solution()

    assert ex.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1, 1, 4, 2, 1, 1, 0, 0]
