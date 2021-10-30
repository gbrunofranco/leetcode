from typing import List
from collections import deque


class Solution:

    def orangesRotting(self, grid):

        row_n, col_n = len(grid), len(grid[0])
        inf = 10 ** 100
        distance = [[inf] * col_n for _ in range(row_n)]
        rotten = deque()

        for x in range(row_n):
            for y in range(col_n):
                if grid[x][y] == 2:
                    distance[x][y] = 0
                    rotten.append((x, y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(rotten) > 0:
            x, y = rotten.popleft()

            for dx, dy in directions:
                nx, ny = x+dx, y+dy

                if 0 <= nx < row_n and 0 <= ny < col_n and distance[nx][ny] == inf and grid[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    rotten.append((nx, ny))

        time = 0
        for x in range(row_n):
            for y in range(col_n):
                if grid[x][y] == 1:
                    time = max(time, distance[x][y])
        if time == inf:
            return -1
        return time


if __name__ == "__main__":
    ex = Solution()

    assert ex.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert ex.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert ex.orangesRotting([[0, 2]]) == 0
