from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        index = 0
        compare_length = len(strs[0])
        joined_strings = "".join(strs)
        removed_columns = set()

        while (index + compare_length) < len(joined_strings):

            if joined_strings[index + compare_length] < joined_strings[index]:
                removed_columns.add(index % compare_length)
            index += 1

        return len(removed_columns)


if __name__ == "__main__":
    sol = Solution()

    assert sol.minDeletionSize(["abc", "bce", "cae"]) == 1
    assert sol.minDeletionSize(["cba", "daf", "ghi"]) == 1
    assert sol.minDeletionSize(["a", "b"]) == 0
    assert sol.minDeletionSize(["zyx", "wvu", "tsr"]) == 3
