from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        temp = []
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != 0:
                i += 1
            else:
                j = i + 1
                while j < n and nums[j] == 0:
                    j += 1
                temp.append(j - i)
                i = j + 1
        ans = sum([sum(range(t+1)) for t in temp])
        return ans


if __name__ == '__main__':
    nums = [1]
    solution = Solution()
    res = solution.zeroFilledSubarray(nums)
    print(res)
