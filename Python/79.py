from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def search_word(pos_x, pos_y, matched_letters=1, matched_positions=None):
            if matched_letters == len(word):
                return True
            for dir_x, dir_y in directions:
                if 0 <= (pos_y + dir_y) and 0 <= (pos_x + dir_x) and (pos_y + dir_y) < rows and (pos_x + dir_x) < columns and board[pos_y + dir_y][pos_x + dir_x] == word[matched_letters] and (pos_x + dir_x, pos_y + dir_y) not in matched_positions:
                    matched_positions.append((pos_x + dir_x, pos_y + dir_y))
                    if search_word(pos_x + dir_x, pos_y +
                                   dir_y, matched_letters + 1, matched_positions):
                        return True
                    matched_positions.pop(-1)
            return False

        rows, columns = len(board), len(board[0])

        for pos_y in range(0, rows):
            for pos_x in range(0, columns):
                if board[pos_y][pos_x] == word[0]:
                    if search_word(pos_x, pos_y, matched_positions=[(pos_x, pos_y)]):
                        return True

        return False


if __name__ == "__main__":
    ex = Solution()

    assert ex.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                    "A", "D", "E", "E"]], "SEE") is True

    assert ex.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                    "A", "D", "E", "E"]], "ABCCED") is True

    assert ex.exist([["a", "b"], ["c", "d"]], "abcd") is False

    assert ex.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], [
                    "A", "D", "E", "E"]], "ABCB") is False

    assert ex.exist([["a", "a"]], "aaa") is False

    assert ex.exist([["C", "A", "A"], ["A", "A", "A"],
                    ["B", "C", "D"]], "AAB") is True
