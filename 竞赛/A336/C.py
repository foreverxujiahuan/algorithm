from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        d_list = []
        bin_len = 20
        for n in nums:
            cur_bin = bin(n)[2:]
            expand_bin = (bin_len - len(cur_bin)) * '0' + cur_bin
            d = dict()
            for i, c in enumerate(expand_bin):
                if c == '1':
                    d[i] = 1
                else:
                    d[i] = 0
            d_list.append(d)
        d_sum_list = [d_list[0]]
        d_tmp = defaultdict(int)
        cur_bool = tuple([d_list[0][i] % 2 == 0 for i in range(bin_len)])
        d_tmp[cur_bool] += 1
        tmp_k = tuple([True for i in range(bin_len)])
        d_tmp[tmp_k] += 1
        for i in range(1, len(d_list)):
            pre_d = d_sum_list[-1]
            cur_d = d_list[i]
            cur_sum_d = dict()
            for k, v in pre_d.items():
                cur_sum_d[k] = pre_d[k] + cur_d[k]
            d_sum_list.append(cur_sum_d)
            cur_bool = tuple([cur_sum_d[i] % 2 == 0 for i in range(bin_len)])
            d_tmp[cur_bool] += 1
        ans = sum([sum(range(s)) for s in d_tmp.values()])
        return ans


if __name__ == '__main__':
    nums = [1, 10, 4]
    solution = Solution()
    res = solution.beautifulSubarrays(nums)
    print(res)