from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        lx_length = len(bin(mx))
        candidates = [n for n in nums if len(bin(n)) == lx_length]
        tmp = 0
        for c in candidates:
            tmp = tmp | c
        cur_mx = -1
        candidate = -1
        for c in candidates:
            if c * (2 ** k) | tmp > cur_mx:
                cur_mx = c * (2 ** k) | tmp
                candidate = c
        index = nums.index(candidate)
        ans = 0
        for i, n in enumerate(nums):
            if i == index:
                ans = ans | (n * (2 ** k))
            else:
                ans = ans | n
        return ans


if __name__ == '__main__':
    solution = Solution()
    # nums = [12, 9]
    # k = 1
    nums = [8, 1, 2]
    k = 2
    # nums = [98, 54, 6, 34, 66, 63, 52, 39, 62, 46, 75, 28, 65, 18, 37, 18, 97, 13, 80, 33, 69, 91, 78, 19, 40]
    # k = 2
    res = solution.maximumOr(nums, k)
    print(res)



