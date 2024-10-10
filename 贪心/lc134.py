from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        length = len(gas)
        while start < length:
            step = 0
            cur_gas = 0
            cur_cost = 0
            while step < length:
                cur_index = (start + step) % length
                cur_gas += gas[cur_index]
                cur_cost += cost[cur_index]
                if cur_gas < cur_cost:
                    break
                step += 1
                if step == length:
                    return start
            start += step + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    res = solution.canCompleteCircuit(gas, cost)
    print(res)


