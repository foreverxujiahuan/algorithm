from typing import List


class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
        target_length = len(supplies) // 2
        cur_supplies = supplies
        target_supplies = []
        while len(cur_supplies) > target_length:
            target_supplies = []
            target_index = -1
            mi_sum = 99999999999
            for i in range(len(cur_supplies) - 1):
                cur_sum = cur_supplies[i] + cur_supplies[i+1]
                if cur_sum < mi_sum:
                    mi_sum = cur_sum
                    target_index = i
            for i in range(len(cur_supplies)):
                if i == target_index:
                    target_supplies.append(mi_sum)
                elif i == target_index + 1:
                    continue
                else:
                    target_supplies.append(cur_supplies[i])
            cur_supplies = target_supplies
        return target_supplies


if __name__ == '__main__':
    supplies = [1,3,1,5]
    solution = Solution()
    res = solution.supplyWagon(supplies)
    print(res)