from typing import List
from string import ascii_lowercase


class Solution:
    def oddString(self, words: List[str]) -> str:
        d = dict()
        for i, c in enumerate(ascii_lowercase):
            d[c] = i
        temp = dict()
        temp2str = dict()
        for i, word in enumerate(words):
            difference = []
            length = len(word)
            for j in range(length - 1):
                difference.append(d[words[i][j+1]] - d[words[i][j]])

            tup = tuple(difference)
            if tup in temp.keys():
                temp[tup] += 1
            else:
                temp[tup] = 1
            temp2str[tup] = word
        for k, v in temp.items():
            if v == 1:
                return temp2str[k]

if __name__ == '__main__':
    words = ["aaa"]
    solution = Solution()
    res = solution.oddString(words)
    print(res)

