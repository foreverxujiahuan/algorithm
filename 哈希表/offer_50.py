class Solution:
    def firstUniqChar(self, s: str) -> str:
        table = dict()
        for c in s:
            if c not in table.keys():
                table[c] = 1
            else:
                table[c] += 1
        for k, v in table.items():
            if v == 1:
                return k
        return " "
