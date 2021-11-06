from typing import List
from heapq import heapify, heappop


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        negative_nums = [-n for n in nums]
        heapify(negative_nums)
        heapify(nums)
        return heappop(negative_nums) * heappop(negative_nums) - heappop(nums) * heappop(nums)


if __name__ == "__main__":
    ex = Solution()

    assert ex.maxProductDifference([5, 6, 2, 7, 4]) == 34
    assert ex.maxProductDifference([4, 2, 5, 9, 7, 4, 8]) == 64
