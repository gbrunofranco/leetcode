from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)

        for node_1, node_2 in edges:
            neighbours[node_1].append(node_2)
            neighbours[node_2].append(node_1)

        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()

            if node == destination:
                return True
            for n in neighbours[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return False


if __name__ == "__main__":
    sol = Solution()

    assert sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) == True
    assert sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) == False
    assert sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 1) == True
    assert sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 2) == True
    assert sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 3, 5) == True
