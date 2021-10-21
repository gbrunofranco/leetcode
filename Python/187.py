from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count = 0
        sequences_count = dict()
        curr_seq = ""
        while count < len(s):
            if len(curr_seq) < 9:
                curr_seq += s[count]
            else:
                curr_seq += s[count]
                if sequences_count.get(curr_seq):
                    sequences_count[curr_seq] = sequences_count.get(curr_seq)+1
                else:
                    sequences_count[curr_seq] = 1
                curr_seq = curr_seq[1:]
            count += 1

        for key, value in list(sequences_count.items()):
            if value == 1:
                del sequences_count[key]
        return list(sequences_count.keys())


if __name__ == "__main__":
    ex = Solution()
    sol = ["AAAAACCCCC", "CCCCCAAAAA"]
    for idx, seq in enumerate(ex.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")):
        assert seq == sol[idx]

    sol = ["AAAAAAAAAA"]
    for idx, seq in enumerate(ex.findRepeatedDnaSequences("AAAAAAAAAAA")):
        assert seq == sol[idx]
