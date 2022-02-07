from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        m = max(milestones)
        t = sum(milestones) - m
        if m > t:
            return 2*t+1
        else:
            return sum(milestones)


if __name__ == '__main__':
    s = Solution()
    milestones = [5,2,1]
    res = s.numberOfWeeks(milestones)
    print(res)
