from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        ans = 0
        d = dict()
        for task in tasks:
            ans += 1
            if task in d.keys():
                ans = max(ans, d[task] + space + 1)
            d[task] = ans
        return ans


if __name__ == '__main__':
    solution = Solution()
    tasks = [1, 2, 1, 2, 3, 1]
    space = 3
    res = solution.taskSchedulerII(tasks, space)
    print(res)
