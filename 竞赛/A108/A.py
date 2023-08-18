from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        ans = -1
        for i in range(length):
            for j in range(i+2, length + 1):
                cur = nums[i: j]
                cur_len = j - i
                if cur[1] - cur[0] != 1:
                    continue
                if cur_len % 2 == 0:
                    if cur == cur[: 2] * (cur_len // 2):
                        ans = max(ans, cur_len)
                else:
                    if cur == cur[: 2] * (cur_len // 2) + [cur[0]]:
                        ans = max(ans, cur_len)
        return ans

if __name__ == '__main__':
    nums = [21,9,5]
    solution = Solution()
    res = solution.alternatingSubarray(nums)
    print(res)