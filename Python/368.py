from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        dp, best = [1]*N, [-1]*N
        ans = []
        max_i = 0

        for i in range(1, N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[i] < (dp[j]+1):
                    dp[i] = dp[j]+1
                    best[i] = j
            if dp[i] > dp[max_i]:
                max_i = i
        while max_i >= 0:
            ans.append(nums[max_i])
            max_i = best[max_i]

        return ans


if __name__ == "__main__":
    ex = Solution()

    assert sorted(ex.largestDivisibleSubset([1, 2, 4, 8])) == [1, 2, 4, 8]
