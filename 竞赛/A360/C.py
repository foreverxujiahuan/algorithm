from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        set_target = []
        set_nums = []
        for n in nums:
            set_nums.append(math.log(n, 2) // 1)
        tmp = math.log(target, 2) // 1
        set_target.append(tmp)
        s = 0
        s += 2 ** tmp
        while s < target:
            if s + 2 ** tmp <= target:
                set_target.append(tmp)
                s += 2 ** tmp
            tmp -= 1
        set_target = [int(i) for i in set_target]
        set_nums = [int(i) for i in set_nums]
        d_target = {i: set_target.count(i) for i in range(32)}
        d_nums = {i: set_nums.count(i) for i in range(32)}
        ans = 0




if __name__ == '__main__':
    nums = [1,2,8]
    target = 7
    solution = Solution()
    res = solution.minOperations(nums, target)
    print(res)

