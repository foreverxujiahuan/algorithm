from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        return sum(tasks) // sessionTime if sum(tasks) % sessionTime == 0 else 1 + (sum(tasks) // sessionTime)


if __name__ == '__main__':
    s = Solution()
    tasks = [9, 6, 9]
    sessionTime = 14
    res = s.minSessions(tasks, sessionTime)
    print(res)
