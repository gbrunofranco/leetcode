from itertools import combinations
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = dict()

        for i in range(len(nums)):
            second_number = target - nums[i]

            if second_number in results.keys():
                return [results[second_number], i]
            else:
                results[nums[i]] = i


if __name__ == "__main__":
    ex = Solution()

    assert ex.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert ex.twoSum([3, 2, 4], 6) == [1, 2]
    assert ex.twoSum([3, 3], 6) == [0, 1]
    assert ex.twoSum([-3, -3], -6) == [0, 1]
    assert ex.twoSum([0, 0], 0) == [0, 1]
