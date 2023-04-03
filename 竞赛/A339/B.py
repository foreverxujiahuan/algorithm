from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        matrix = []
        cnt = len(nums)
        while cnt:
            cur = []
            for k, v in counter.items():
                if v > 0:
                    cur.append(k)
                    counter[k] -= 1
                    cnt -= 1
            matrix.append(cur)
        return matrix


if __name__ == '__main__':
    nums = [1,2,3,4]
    solution = Solution()
    res = solution.findMatrix(nums)
    print(res)