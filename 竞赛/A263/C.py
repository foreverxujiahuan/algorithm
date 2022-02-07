from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        sub2value = dict()
        sub_list = self.get_sub_list(nums)
        for sub in sub_list:
            value = self.get_value(sub)
            if value in sub2value.keys():
                sub2value[value] += 1
            else:
                sub2value[value] = 1
        return sub2value[max(sub2value.keys())]

    def get_value(self, sub):
        cur = 0
        for n in sub:
            cur = cur | n
        return cur

    def get_sub_list(self, numbers):
        if len(numbers) == 0:
            return [[]]
        return self.get_sub_list(numbers[1:]) + [[numbers[0]] + r for r in self.get_sub_list(numbers[1:])]


if __name__ == '__main__':
    nums = [2, 2, 2]
    s = Solution()
    res = s.countMaxOrSubsets(nums)
    print(res)
    # for i, t in enumerate()