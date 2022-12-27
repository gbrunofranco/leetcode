from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additional_rocks: int) -> int:
        for index, d in enumerate(sorted([c - r for c, r in zip(capacity, rocks)])):
            if d > additional_rocks:
                return index
            additional_rocks -= d
        return len(capacity)


if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2) == 3
    assert sol.maximumBags([10, 2, 2], [2, 2, 0], 100) == 3
