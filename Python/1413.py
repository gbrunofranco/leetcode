from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_value, tot_sum, idx = 0, 0, 0
        while idx < len(nums):
            tot_sum += nums[idx]
            if tot_sum < start_value:
                start_value = tot_sum
            idx += 1
        return -start_value + 1


if __name__ == "__main__":
    ex = Solution()

    assert ex.minStartValue([[-3, 2, -3, 4, 2]]) == 5
    assert ex.minStartValue([1, 2]) == 1
