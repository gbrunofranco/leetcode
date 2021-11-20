from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, mid, end = 0, 0, len(nums) // 2

        while start < end:
            mid = (end + start) // 2
            if nums[mid*2] == nums[mid*2+1]:
                start = mid + 1
            else:
                end = mid

        return nums[start*2]


if __name__ == "__main__":
    ex = Solution()
    assert ex.singleNonDuplicate([1]) == 1

    assert ex.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]) == 8
    assert ex.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert ex.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
