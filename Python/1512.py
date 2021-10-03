from itertools import combinations
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for pair in combinations(nums, 2):
            if pair[0] == pair[1]:
                count += 1
        return count

if __name__ == "__main__":
    ex = Solution()

    assert ex.numIdenticalPairs([1,2,3,1,1,3]) == 4
    assert ex.numIdenticalPairs([1,1,1,1]) == 6
    assert ex.numIdenticalPairs([1,2,3]) == 0
