from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        mx, mi = max(salary), min(salary)
        salary = [s for s in salary if s not in {mx, mi}]
        return sum(salary) / len(salary)