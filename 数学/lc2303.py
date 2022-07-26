from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        t = income
        last_upper = 0
        for upper, percent in brackets:
            if t <= 0:
                break
            cur = min(t, upper - last_upper)
            t = income - upper
            res += (cur * percent) / 100
            last_upper = upper
        return res


if __name__ == '__main__':
    brackets = [[2,50]]
    income = 0
    solution = Solution()
    res = solution.calculateTax(brackets, income)
    print(res)