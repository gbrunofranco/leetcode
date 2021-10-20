class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift


if __name__ == "__main__":
    ex = Solution()

    assert ex.rangeBitwiseAnd(5, 7) == 4
    assert ex.rangeBitwiseAnd(0, 0)
    assert ex.rangeBitwiseAnd(1, 2147483647)
