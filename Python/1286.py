from itertools import combinations
from math import factorial


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = combinations(characters, combinationLength)
        self.count = 0
        self.total = int(factorial(len(
            characters))/(factorial(len(characters)-combinationLength)*factorial(combinationLength)))

    def next(self) -> str:
        self.count += 1
        return "".join(next(self.combinations))

    def hasNext(self) -> bool:
        if self.count < self.total:
            return True
        return False


if __name__ == "__main__":
    iterator = CombinationIterator("abc", 2)

    assert iterator.next() == "ab"
    assert iterator.hasNext() is True
    assert iterator.next() == "ac"
    assert iterator.hasNext() is True
    assert iterator.next() == "bc"
    assert iterator.hasNext() is False
