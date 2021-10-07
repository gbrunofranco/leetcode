from typing import List, Set


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = (front_elem for idx, front_elem in enumerate(
            fronts) if front_elem == backs[idx])
        complete = (set(fronts) | set(backs)) - set(invalid)
        if len(complete) == 0:
            return 0
        return sorted(complete)[0]


if __name__ == "__main__":
    ex = Solution()

    print(ex.flipgame([1, 2, 4, 4, 7], [1, 3, 4, 1, 3]))
