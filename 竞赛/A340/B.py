from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        ni2index = dict()
        for i, n in enumerate(nums):
            d[n].append(i)
            ni2index[(n, i)] = len(d[n]) - 1
        n2pre = dict()
        for k, v in d.items():
            n2pre[k] = list(accumulate(v))

        ans = []
        for j, m in enumerate(nums):
            pre = n2pre[m]
            n = j
            i = ni2index[(m, j)]
            leng = len(pre)
            tmp1 = pre[-1] - pre[i] - n * (leng - i)
            tmp2 = (n * i) - pre[i]
            cur = tmp1 + tmp2
            ans.append(cur)
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,1,1,2]
    res = solution.distance(nums)
    print(res)