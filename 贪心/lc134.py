from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if self.flag(gas, cost, i):
                return i
        return -1

    def flag(self, gas, cost, index):
        cur_gas = 0
        for i in range(index, len(gas)):
            cur_gas += gas[i]
            cur_gas -= cost[i]
            if cur_gas < 0:
                return False
        for i in range(index):
            cur_gas += gas[i]
            cur_gas -= cost[i]
            if cur_gas < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    res = s.canCompleteCircuit(gas, cost)
    print(res)