from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_count, ones_count, twos_count = 0, 0, 0
        for number in nums:
            if number == 0:
                zeros_count += 1
            elif number == 1:
                ones_count += 1
            else:
                twos_count += 1

        nums[:zeros_count] = [0]*zeros_count
        nums[zeros_count:zeros_count+ones_count] = [1]*ones_count
        nums[zeros_count+ones_count:zeros_count +
             ones_count+twos_count] = [2]*twos_count


if __name__ == "__main__":
    ex = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    ex.sortColors(nums)
    assert all(res is True for res in [
               x == y for (x, y) in zip(nums, [0, 0, 1, 1, 2, 2])])

    nums = [2, 0, 1]
    ex.sortColors(nums)
    assert all(res is True for res in [
               x == y for (x, y) in zip(nums, [0, 1, 2])])

    nums = [0]
    ex.sortColors(nums)
    assert all(res is True for res in [
               x == y for (x, y) in zip(nums, [0])])

    nums = [1]
    ex.sortColors(nums)
    assert all(res is True for res in [
               x == y for (x, y) in zip(nums, [1])])
