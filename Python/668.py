class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        k -= 1
        left = 1
        right = m * n

        def count(x):
            c = 0
            for i in range(1, m+1):
                c += min(n, (x-1) // i)
            return c

        while left < right:
            mid = (left + right + 1) // 2
            if count(mid) > k:
                right = mid - 1
            else:
                left = mid

        return left


if __name__ == "__main__":
    ex = Solution()

    assert ex.findKthNumber(3, 3, 5) == 3
    assert ex.findKthNumber(2, 3, 6) == 6
