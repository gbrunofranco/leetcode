from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_n, col_n = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        to_check = deque()
        for x in range(col_n):
            for y in range(row_n):
                if board[y][x] == "O":
                    if x == 0 or x == col_n - 1 or y == 0 or y == row_n - 1:
                        to_check.append((x, y))
                        board[y][x] = "F"

        while len(to_check) > 0:
            x, y = to_check.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < col_n and 0 <= ny < row_n and board[ny][nx] == "O":
                    board[ny][nx] = "F"
                    to_check.append((nx, ny))

        for x in range(col_n):
            for y in range(row_n):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "F":
                    board[y][x] = "O"


if __name__ == "__main__":
    ex = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

    sol = [["X", "X", "X", "X"], ["X", "X", "X", "X"],
           ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    ex.solve(board)

    for sol_row, board_row in zip(sol, board):
        for sol_elem, board_elem in zip(sol_row, board_row):
            assert sol_elem == board_elem

    board = [["X", "X", "O", "X"], ["X", "O", "O", "O"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    sol = [["X", "X", "O", "X"], ["X", "O", "O", "O"],
           ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

    ex.solve(board)
    for sol_row, board_row in zip(sol, board):
        for sol_elem, board_elem in zip(sol_row, board_row):
            assert sol_elem == board_elem
