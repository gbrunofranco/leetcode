class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0

        while xor:
            res += xor & 1
            xor >>= 1

        return res


if __name__ == "__main__":
    ex = Solution()

    assert ex.hammingDistance(1, 3) == 1
    assert ex.hammingDistance(1, 4) == 2
