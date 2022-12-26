from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        total_jumped = 0

        for index, jump in enumerate(nums):
            if index <= total_jumped:
                total_jumped = max(index + jump, total_jumped)

        return total_jumped >= len(nums) - 1


if __name__ == "__main__":
    sol = Solution()

    assert sol.canJump([2, 3, 1, 1, 4]) == True
    assert sol.canJump([3, 2, 1, 0, 4]) == False
    assert sol.canJump([2, 0, 0]) == True
    assert sol.canJump([3, 0, 8, 2, 0, 0, 1]) == True
