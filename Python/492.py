from typing import List
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        root: float = sqrt(area)

        if (root.is_integer()):
            return [int(root), int(root)]

        factors = self.divisors(area)
        sorted_factors = sorted(factors, reverse=True)
        for idx, _ in enumerate(sorted_factors):
            if sorted_factors[idx]*sorted_factors[idx+1] <= area:
                return [sorted_factors[idx], sorted_factors[idx+1]]

    # function from: https://stackoverflow.com/a/37058745 and https://alexwlchan.net/2019/07/finding-divisors-with-python/
    @staticmethod
    def divisors(n):
        # get factors and their counts
        factors = {}
        nn = n
        i = 2
        while i*i <= nn:
            while nn % i == 0:
                factors[i] = factors.get(i, 0) + 1
                nn //= i
            i += 1
        if nn > 1:
            factors[nn] = factors.get(nn, 0) + 1

        primes = list(factors.keys())


        # generates factors from primes[k:] subset
        def generate(k):
            if k == len(primes):
                yield 1
            else:
                rest = generate(k+1)
                prime = primes[k]
                for factor in rest:
                    prime_to_i = 1
                    # prime_to_i iterates prime**i values, i being all possible exponents
                    for _ in range(factors[prime] + 1):
                        yield factor * prime_to_i
                        prime_to_i *= prime

        # in python3, `yield from generate(0)` would also work
        for factor in generate(0):
            yield factor


if __name__ == "__main__":
    ex = Solution()
    assert ex.constructRectangle(122122) == [427, 286]
    assert ex.constructRectangle(37) == [37, 1]
    assert ex.constructRectangle(4) == [2, 2]
