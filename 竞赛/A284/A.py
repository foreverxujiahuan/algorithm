from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        length = len(nums)
        res = []
        for i in range(length):
            for j in range(length):
                if abs(i - j) <= k and nums[j] == key:
                    res.append(i)
                    break
        return res

if __name__ == '__main__':
    nums = [2,2,2,2,2]
    key = 2
    k = 2
    s = Solution()
    res = s.findKDistantIndices(nums, key, k)
    print(res)