from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = dict()
        for n in nums:
            cur_s = ""
            str_n = str(n)
            for ch in str_n:
                cur_s += str(mapping[int(ch)])
            d[n] = int(cur_s)
        return sorted(nums, key=lambda n: d[n])


if __name__ == '__main__':
    solution = Solution()
    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = [789, 456, 123]
    res = solution.sortJumbled(mapping, nums)
    print(res)