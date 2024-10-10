from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1]
        R = [1]
        for i in nums[:-1]:
            L.append(i * L[-1])
        for i in reversed(nums[1:]):
            R.append(i * R[-1])
        R.reverse()
        ans = [L[i] * R[i] for i in range(len(nums))]
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [-1,1,0,-3,3]
    res = solution.productExceptSelf(nums)
    print(res)
