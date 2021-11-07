class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num):
            counter = 0
            tot = 0
            while counter < len(num):
                tot *= 10
                tot += int(num[counter])
                counter += 1
            return tot

        return str(convert(num1)*convert(num2))


if __name__ == "__main__":
    ex = Solution()

    assert ex.multiply("2", "3") == "6"
    assert ex.multiply("123", "456") == "56088"
    assert ex.multiply("0", "456") == "0"
    assert ex.multiply("0", "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890") == "0"
