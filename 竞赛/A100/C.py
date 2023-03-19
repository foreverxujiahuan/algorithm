from collections import Counter, defaultdict
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        d_list = defaultdict(list)
        for i, n in enumerate(nums):
            d_list[n].append(i)
        sorted_nums = list(sorted(set(nums)))
        ans = 0
        remove_index = set()
        for n in sorted_nums:
            for index in d_list[n]:
                if index in remove_index:
                    continue
                ans += n
                remove_index.add(index-1)
                remove_index.add(index+1)
        return ans


if __name__ == '__main__':
    nums = [10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42] * 10000
    solution = Solution()
    res = solution.findScore(nums)
    print(res)
    # 1700042