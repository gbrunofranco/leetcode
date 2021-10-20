from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 1), (1, 0), (0, 1), (-1, -1),
                      (-1, 0), (0, -1), (-1, 1), (1, -1)]

        rows, columns = len(board), len(board[0])
        position_x, position_y = 0, 0

        positions_to_change = set()
        while position_x < columns and position_y < rows:
            count_zeroes, count_ones = 0, 0
            for dir_x, dir_y in directions:
                if 0 <= position_x + dir_x < columns and 0 <= position_y + dir_y < rows:
                    if board[position_y + dir_y][position_x+dir_x] == 1:
                        count_ones += 1
                    else:
                        count_zeroes += 1

            if board[position_y][position_x] == 1 and (count_ones < 2 or count_ones > 3):
                positions_to_change.add((position_x, position_y))
            elif board[position_y][position_x] == 0 and count_ones == 3:
                positions_to_change.add((position_x, position_y))

            position_x += 1
            if position_x == columns:
                position_x = 0
                position_y += 1

        for pos_x, pos_y in positions_to_change:
            if board[pos_y][pos_x] == 1:
                board[pos_y][pos_x] = 0
            else:
                board[pos_y][pos_x] = 1


if __name__ == "__main__":
    ex = Solution()
    board = [[1, 1], [1, 0]]
    ex.gameOfLife(board)
    assert board == [[1, 1], [1, 1]]
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    ex.gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
