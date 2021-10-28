from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for left_idx in range(len(nums)):
            if left_idx > 0 and nums[left_idx] == nums[left_idx - 1]:
                continue

            increment = 1
            right_idx = len(nums) - 1
            required_sum = -nums[left_idx]

            while left_idx + increment < right_idx:
                current_sum = nums[left_idx + increment] + nums[right_idx]

                if current_sum < required_sum:
                    increment += 1
                elif current_sum > required_sum:
                    right_idx -= 1
                else:
                    result.append(
                        [nums[left_idx], nums[left_idx + increment], nums[right_idx]])
                    increment += 1
                    while left_idx + increment < right_idx and nums[left_idx + increment] == nums[left_idx + increment - 1]:

                        increment += 1
        return result


if __name__ == "__main__":
    ex = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    sol = [[-1, -1, 2], [-1, 0, 1]]

    for sol_l, res_l in zip(sol, ex.threeSum(nums)):
        assert all(res is True for res in [
            x == y for (x, y) in zip(sol_l, res_l)])
