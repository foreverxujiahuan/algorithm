from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_v = max(nums)
        ans = 1
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == max_v:
                j = i + 1
                while j < length and nums[j] == max_v:
                    ans = max(j - i + 1, ans)
                    j += 1
                i = j + 1
            i += 1
        return ans


if __name__ == '__main__':
    nums = [395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,395808,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,470030,153490,330001,330001,330001,330001,330001,330001,330001,37284,470030,470030,470030,470030,470030,470030,156542,226743]
    solution = Solution()
    res = solution.longestSubarray(nums)
    print(res)


