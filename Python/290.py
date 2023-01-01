class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        mapping_word_letter = {}
        mapping_letter_word = {}

        if len(pattern) != len(words):
            return False

        for word, letter in zip(words, pattern):
            if (mapping_word_letter.get(word) and mapping_word_letter.get(word) != letter) or (
                mapping_letter_word.get(letter) and mapping_letter_word.get(letter) != word
            ):
                return False
            mapping_word_letter[word] = letter
            mapping_letter_word[letter] = word
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.wordPattern("abba", "dog cat cat dog") == True
    assert sol.wordPattern("abba", "dog cat cat fish") == False
    assert sol.wordPattern("aaaa", "dog cat cat dog") == False
