from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        new_s = list()
        for letter, value in Counter(s).most_common():
            new_s.append(letter*value)
        return "".join(new_s)


if __name__ == "__main__":
    ex = Solution()

    assert ex.frequencySort("cccaaa") == "aaaccc" or ex.frequencySort(
        "cccaaa") == "cccaaa"

    assert ex.frequencySort(
        "tree") == "eert" or ex.frequencySort("tree") == "eetr"
