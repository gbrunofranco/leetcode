class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [0, 1, 2, 5] + [0] * 997

        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]

        return dp[n] % MOD


if __name__ == "__main__":
    sol = Solution()

    assert sol.numTilings(1) == 1
    assert sol.numTilings(2) == 2
    assert sol.numTilings(3) == 5
    assert sol.numTilings(6) == 53
    assert sol.numTilings(7) == 117
    assert sol.numTilings(100) == 190242381
