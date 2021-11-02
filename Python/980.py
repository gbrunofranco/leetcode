from typing import List
from collections import deque


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        row_n, col_n = len(grid), len(grid[0])
        to_check, results = list(), list()
        starting, ending = list(), tuple()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x in range(row_n):
            for y in range(col_n):
                if grid[x][y] == 0:
                    to_check.append((x, y))
                elif grid[x][y] == 1:
                    starting = [(x, y)]
                elif grid[x][y] == 2:
                    ending = (x, y)

        walk_length = len(to_check) + 1

        def search(visited=None):
            if visited is None:
                visited = starting
            x, y = visited[-1]

            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if (nx, ny) in to_check and (nx, ny) not in visited:
                    search(visited + [(nx, ny)])
            if len(visited) == walk_length:
                for dx, dy in directions:
                    nx, ny = x + dx, y+dy
                    if 0 <= nx < row_n and 0 <= ny < col_n and (nx, ny) == ending:
                        results.append(visited)
        search()
        return len(results)


if __name__ == "__main__":
    ex = Solution()

    assert ex.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
    assert ex.uniquePathsIII([[0, 1], [2, 0]]) == 0
    assert ex.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
    assert ex.uniquePathsIII([[1], [2]]) == 1
    assert ex.uniquePathsIII(
        [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 2, -1, 0, 0]]) == 2
