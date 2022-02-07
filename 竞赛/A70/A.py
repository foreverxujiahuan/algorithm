from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        length = len(cost)
        cnt = length // 3
        output = []
        cnt += 1
        res = 0
        cost = sorted(cost, reverse=True)
        for i in range(cnt):
            temp = cost[i*3: (i+1)*3]
            output.append(temp)
        for t in output:
            if len(t) == 3:
                res += sum(t[:2])
            else:
                res += sum(t)
        return res

if __name__ == '__main__':
    cost = [1,2,3]
    solution = Solution()
    res = solution.minimumCost(cost)
    print(res)
