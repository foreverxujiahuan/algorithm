from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        res = []
        self.dfs(length, '', res, 0)
        nums = set(nums)
        print(res)
        for t in res:
            if t not in nums:
                return t

    def dfs(self, length, cur, res, index):
        if index == length:
            res.append(cur)
            return
        self.dfs(length, cur + '1', res, index+1)
        self.dfs(length, cur + '0', res, index+1)


if __name__ == '__main__':
    s = Solution()
    nums = ["111","011","001"]
    res = s.findDifferentBinaryString(nums)
    print(res)