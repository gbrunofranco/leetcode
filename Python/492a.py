from typing import List
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        root: float = sqrt(area)

        if (root.is_integer()):
            return [int(root), int(root)]

        factors = self.divisors(area)
        sorted_factors = sorted(factors, reverse=True)
        for idx, _ in enumerate(sorted_factors):
            if sorted_factors[idx]*sorted_factors[idx+1] <= area:
                return [sorted_factors[idx], sorted_factors[idx+1]]


if __name__ == "__main__":
    ex = Solution()
    assert ex.constructRectangle(122122) == [427, 286]
    assert ex.constructRectangle(37) == [37, 1]
    assert ex.constructRectangle(4) == [2, 2]
