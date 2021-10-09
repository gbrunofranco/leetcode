from itertools import permutations
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()
        for string in strs:
            s_string = "".join(sorted(string))
            if s_string not in dictionary:
                dictionary[s_string] = [string]
            else:
                dictionary[s_string].append(string)
        return dictionary.values()


if __name__ == "__main__":
    ex = Solution()

    res = ex.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    sol = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    count = 0
    for sublist_sol in sol:
        for sublists_res in res:
            if sorted(sublist_sol) == sorted(sublists_res):
                count += 1
                break
    assert count == len(sol)

    assert list(ex.groupAnagrams([""])) == [[""]]

    assert list(ex.groupAnagrams(["a"])) == [["a"]]
