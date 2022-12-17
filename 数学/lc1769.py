from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        ans = [0] * l
        for i in range(l):
            cnt = 0
            for j in range(l):
                if j == i:
                    continue
                if boxes[j] == '0':
                    continue
                cnt += abs(j-i)
            ans[i] = cnt
        return ans
