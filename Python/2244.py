from typing import List
import collections


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter_map = collections.Counter(tasks)
        steps = 0
        for value in counter_map.values():
            if value == 1:
                return -1

            steps += round(value + 2) // 3
        return steps


if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumRounds([2, 3, 3]) == -1
    assert sol.minimumRounds([3, 3, 3, 3, 3]) == 2
    assert sol.minimumRounds([3, 3, 3, 3, 3, 3]) == 2
    assert sol.minimumRounds([3, 3, 3, 3, 3, 3, 3]) == 3
    assert sol.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4
