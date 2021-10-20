from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        total_rows, total_cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def depth_first_search(x, y):

            for dx, dy in directions:
                position_x, position_y = x+dx, y+dy

                if 0 <= position_x < total_rows and 0 <= position_y < total_cols and board[position_x][position_y] == "O" and (position_x, position_y) not in visited:
                    visited.add((position_x, position_y))
                    board[position_x][position_y] = "#"
                    depth_first_search(position_x, position_y)

        for x in range(total_rows):
            for y in range(total_cols):
                if (x == 0 or x == total_rows-1 or y == 0 or y == total_cols-1) and board[x][y] == "O" and (x, y) not in visited:
                    visited.add((x, y))
                    board[x][y] = "#"
                    depth_first_search(x, y)

        for x in range(total_rows):
            for y in range(total_cols):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "#":
                    board[x][y] = "O"


if __name__ == "__main__":
    ex = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    ex.solve(board)
    sol = [["X", "X", "X", "X"], ["X", "X", "X", "X"],
           ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
    for board_elem, sol_elem in zip(board, sol):
        assert board_elem == sol_elem

    board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], [
        "X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]
    ex.solve(board)
    sol = [["O", "X", "X", "O", "X"], ["X", "X", "X", "X", "O"], [
        "X", "X", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]

    for board_elem, sol_elem in zip(board, sol):
        assert board_elem == sol_elem
