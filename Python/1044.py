from functools import cache


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        #                Suffixes        Indexes           Starting Indexes
        #
        #                banana          012345            0
        #                anana           12345             1
        # banana ------> nana   ------>  2345    ------->  2
        #                ana             345               3
        #                na              34                4
        #                a               5                 5
        #
        #                 |
        #                 | Sort
        #                 |
        #                 |              Lenghts
        #                 v
        #               a                1
        #               ana              3
        #               anana            5
        #               banana  ------>  6
        #               na               2
        #               nana             4
        #
        #
        #
        #               The longest substring will be part of the suffixes
        #
        #               We can get back to the substring by having the starting index and its length
        #
        #               The idea is that if we're checking for substrings matching "ana" if we previously
        #                 searched for the substrings "a" and "na" we already know if "ana" can be the best
        #                 string. If there are multiple matching of the substrings "a" and "na" then "ana"
        #                 can be the best string otherwise it cannot.

        s_len = len(s)
        indexes = list(range(s_len))

        indexes.sort(key=lambda x: s[x:])

        best_length, best_start = 0, None

        @cache
        def get_match_length(i, j):
            if i >= s_len:
                return 0
            if j >= s_len:
                return 0
            if s[i] != s[j]:
                return 0
            return 1 + get_match_length(i+1, j+1)

        for i in range(1, s_len):
            L = get_match_length(indexes[i], indexes[i - 1])
            if best_length < L:
                best_length = L
                best_start = indexes[i]

        if best_start is None:
            return ""
        return s[best_start:best_start + best_length]


if __name__ == "__main__":
    ex = Solution()

    assert ex.longestDupSubstring("banana") == "ana"
    assert ex.longestDupSubstring("abcd") == ""
    assert ex.longestDupSubstring(
        "nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy") == "ma"
