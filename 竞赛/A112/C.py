from collections import Counter
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        length = len(nums)
        counter = Counter(nums[: k])
        mx = 0
        if len(counter.keys()) >= m:
            mx = sum(nums[: k])
        cur_sum = sum(nums[: k])
        for i in range(k, length):
            counter[nums[i]] += 1
            cur = nums[i - k]
            counter[cur] -= 1
            cur_sum += nums[i]
            cur_sum -= cur
            if counter[cur] == 0:
                del counter[cur]
            if len(counter.keys()) >= m:
                mx = max(mx, cur_sum)
        return mx

if __name__ == '__main__':
    nums = [1,1,3,3]
    m = 2
    k = 2
    solution = Solution()
    res = solution.maxSum(nums, m, k)
    print(res)


