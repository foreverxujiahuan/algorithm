from typing import List
from collections import defaultdict


class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        head_d = defaultdict(int)
        tail_d = defaultdict(int)
        for word in words:
            head_d[word[0]] += 1
            tail_d[word[-1]] += 1
        ans = sum([len(word) for word in words])
        for k in head_d.keys():
            ans -= min(head_d[k], tail_d[k])
        return ans



if __name__ == '__main__':
    pass

