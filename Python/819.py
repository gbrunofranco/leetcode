from collections import Counter
from re import split
from typing import List, Tuple


# Type hints bring this to 48 ms 14.3 MB instead of 28 ms 14.4 MB
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_count: Counter = Counter(split(";|\ |\?|!|,|\.|'", paragraph.lower()))
        most_common: List[Tuple[str, int]] = words_count.most_common()
        for word, _ in most_common:
            if word not in banned and len(word) > 0:
                return word

if __name__ == "__main__":
    ex = Solution()
    assert ex.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball"
    assert ex.mostCommonWord("a.", []) == "a"
    assert ex.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]) == "ball"
