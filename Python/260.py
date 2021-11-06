from typing import List
from functools import cache


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
                                                                            and with
            Dec                           Bin          element-wise XOR     negative                                        element-wise AND with the
                                                                            value                                           "truncated" mask, these creates
        [1, 2, 1, 3, 2, 5]  +-------->  [1,10,1,11,10,101]  +-------->  110  +-------->  10   +------------------------>    two cases: THE AND can have at least
                                                                                                                            a 1 digit or have every digit to 0.
                +                                                        +                +                                  
                |                                                        |                |                                  In our example:
                |                                                        |                |                                  1 & 10 -> 0
                |                                                        |                |                                  101 & 01 -> 0
                |                                                        |                |                                  So we do 1 ^ 1 ^ 101 -> 101 = x
                v                                                        v                |
            We want 3,5                                            The pair values        |                                  11 & 10 -> 10
            as x, y                                                XOR to 0, the          |                                  10 & 10 -> 10
                                                                   result is x^y          v
                                                                        +                                                    So we do 10 ^ 11 ^ 10 -> 11 = y
                                                                        |           We want the least possible
                                                                        |           difference so we take the
                                                                        +------->   right most 1 with the
                                                                                    trailing zeros

                                                                                        +
                                                                                        |
                                                                                        |
                                                                                        |
                                                                                        |
                                                                                        v

                                                                                    The least possible difference
                                                                                    is the least possible value
                                                                                    of x or y
        """
        bit_diff = 0

        for n in nums:
            bit_diff = bit_diff ^ n

        mask = bit_diff & -bit_diff

        x, y = 0, 0
        for n in nums:
            if n & mask:
                x = x ^ n
            else:
                y = y ^ n

        return x, y


if __name__ == "__main__":
    ex = Solution()

    assert ex.singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5] or [5, 3]
