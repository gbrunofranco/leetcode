class Solution:
    def numTrees(self, n: int) -> int:
        cache = [None]*(n+1)  # n + 1 because we call count() with 0

        def count(x):
            if x <= 1:  # We call count() with 0 but it's a multiplication so we want it to return 1
                return 1

            if cache[x] is not None:
                return cache[x]

            total_count = 0

            for right in range(0, x):
                left = x - right - 1
                total_count += count(left)*count(right)

            cache[x] = total_count
            return total_count

        return count(n)


if __name__ == "__main__":
    ex = Solution()

    assert ex.numTrees(1) == 1
    assert ex.numTrees(3) == 5
