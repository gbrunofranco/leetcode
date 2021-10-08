class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        current_elem = 1
        previous_elem = 0
        total = 0

        for idx in range(1, len(s)):
            if s[idx] == s[idx-1]:  # no change, we can keep counting the same digit
                current_elem += 1
            else:
                # there's a change so we add the minimum length between the current
                # and previous element and then reset: the count of the current element
                # becomes the count of the previous one and current becomes 1
                total += min(current_elem, previous_elem)
                previous_elem = current_elem
                current_elem = 1
        return total + min(current_elem, previous_elem)


if __name__ == "__main__":
    ex = Solution()

    assert ex.countBinarySubstrings("00110011") == 6
    assert ex.countBinarySubstrings("10101") == 4
