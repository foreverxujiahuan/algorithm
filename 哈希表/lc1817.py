from typing import List
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user2value = defaultdict(list)
        for log in logs:
            user, t = log
            if t not in user2value[user]:
                user2value[user].append(t)
        value2users = defaultdict(int)
        for user, value in user2value.items():
            value2users[len(value)] += 1
        ans = [0 for _ in range(k)]
        for value, users in value2users.items():
            ans[value-1] = users
        return ans


if __name__ == '__main__':
    logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
    k = 5
    solution = Solution()
    res = solution.findingUsersActiveMinutes(logs, k)
    print(res)
