from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                ans[stack[-1]] = -stack[-1] + index
                stack.pop()
            stack.append(index)
        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
