from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        if nums[low] < nums[high]:
            return nums[low]

        while low < high:
            mid = int(low + (high - low) / 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1

        return nums[high]


if __name__ == "__main__":
    ex = Solution()

    assert ex.findMin([1, 3, 5]) == 1
    assert ex.findMin([2, 2, 2, 0, 1]) == 0
    assert ex.findMin([2, 2, 2, 1]) == 1
    assert ex.findMin([10, 10, 10, 1, 10]) == 1
    assert ex.findMin([0, 1]) == 0
    assert ex.findMin([4, 5, 6, 7, 0, 1, 4]) == 0
    assert ex.findMin([0, 1, 4, 4, 5, 6, 7]) == 0
    assert ex.findMin([0]) == 0
    assert ex.findMin([1, 0]) == 0
