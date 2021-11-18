from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        total_nums = range(1, len(nums)+1)
        return set(total_nums) - set(nums)


if __name__ == "__main__":
    ex = Solution()

    assert list(ex.findDisappearedNumbers([1, 1])) == [2]
    assert list(ex.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])) == [5, 6]
