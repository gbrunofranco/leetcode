from math import sqrt


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # spaces = x*(x+1) // 2
        # N <= spaces = x*(x+1) // 2
        # 2N = x^2 + x -> x^2 + x - 2N
        # x = (-1+-sqrt(1+8N))//2
        return int((-1+sqrt(1+8*n))//2)


if __name__ == "__main__":
    ex = Solution()

    ex.arrangeCoins(5) == 2
    ex.arrangeCoins(8) == 3
    ex.arrangeCoins(1) == 1
    ex.arrangeCoins(1000000) == 1413
