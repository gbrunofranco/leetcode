from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        k = 0
        bought = 0
        max_cost, min_cost = max(costs), min(costs)
        counters = [0] * (max_cost + 1)

        for cost in costs:
            counters[cost - min_cost] += 1
        for index in range(len(counters)):
            while counters[index] > 0:
                costs[k] = index + min_cost
                counters[index] -= 1
                coins -= costs[k]
                k += 1

                if coins < 0:
                    return bought
                bought += 1
        return bought


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxIceCream([1, 3, 2, 4, 1], 7) == 4
    assert sol.maxIceCream([10, 6, 8, 7, 7, 8], 5) == 0
    assert sol.maxIceCream([1, 6, 3, 1, 2, 5], 20) == 6
