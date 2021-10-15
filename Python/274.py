from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = [0] * (len(citations) + 1)
        for c in citations:
            papers[min(len(citations), c)] += 1
        idx = len(citations)
        s = papers[len(citations)]
        while idx > s:
            idx -= 1
            s += papers[idx]
        return idx


if __name__ == "__main__":
    ex = Solution()

    assert ex.hIndex([3, 0, 6, 1, 5]) == 3
    assert ex.hIndex([1, 3, 1]) == 1
    assert ex.hIndex([0]) == 0
    assert ex.hIndex([100]) == 1
