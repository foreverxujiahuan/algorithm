from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        valid_set = set()
        length = len(nums)
        res = 0
        for i in range(length):
            for j in range(i+1, length+1):
                cur_list = nums[i: j]
                cur_tuple = tuple(cur_list)
                if cur_tuple in valid_set:
                    continue
                count = 0
                for t in cur_list:
                    if t % p == 0:
                        count += 1
                    if count > k:
                        break
                if count <= k:
                    valid_set.add(cur_tuple)
                    res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    k = 4
    p = 1
    res = solution.countDistinct(nums, k, p)
    print(res)
