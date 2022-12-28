from typing import List
import heapq
from math import floor


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        negative_piles = [-pile for pile in piles]
        heapq.heapify(negative_piles)
        for _ in range(k):
            heapq.heapreplace(negative_piles, floor(negative_piles[0] / 2))
        return -sum(negative_piles)


if __name__ == "__main__":
    sol = Solution()

    assert sol.minStoneSum([5, 4, 9], 2) == 12
    assert sol.minStoneSum([4, 3, 6, 7], 3) == 12
