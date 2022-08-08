from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = dict()
        for item in items1:
            v, w = item
            if v in d.keys():
                d[v] += w
            else:
                d[v] = w
        for item in items2:
            v, w = item
            if v in d.keys():
                d[v] += w
            else:
                d[v] = w
        ans = []
        for k in sorted(d.keys()):
            ans.append([k, d[k]])
        return ans

