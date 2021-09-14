from math import dist
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        if p1 == p2 == p3 == p4:
            return False

        distances = [dist(p1, p2), dist(p1, p3), dist(p1, p4),
                     dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        distances.sort()

        if distances[0] == distances[1] == distances[2] == distances[3]:
            if distances[4] == distances[5]:
                return True

        return False


if __name__ == "__main__":
    ex = Solution()
    assert ex.validSquare([0, 0], [1, 1], [1, 0], [0, 1]) == True
    assert ex.validSquare([1, 0], [-1, 0], [0, 1], [0, -1]) == True
    assert ex.validSquare([6987, -473], [6985, -473],
                          [6986, -472], [6986, -474]) == True
    assert ex.validSquare([0, 0], [1, 1], [1, 0], [0, 12]) == False
    assert ex.validSquare([0, 0], [1, 1], [0, 0], [1, 1]) == False
    assert ex.validSquare([-792, -1897], [-150, -3181],
                          [492, -1255], [1134, -2539]) == True
    assert ex.validSquare([1134, -2539], [492, -1255],
                          [-792, -1897], [-150, -3181]) == True
