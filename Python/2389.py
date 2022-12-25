from typing import List
import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        prefix = [0]

        prefix.extend(prefix[-1] + number for number in nums)

        for query in queries:
            index = bisect.bisect_right(prefix, query)
            ans.append(index - 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.answerQueries([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]
    assert sol.answerQueries([2, 3, 4, 5], [1])
    assert sol.answerQueries([4, 5, 2, 1, 3, 6], [3, 10, 21]) == [2, 4, 6]
