from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides = [t for t in rides if t[1] <= n]
        rides = sorted(rides, key=lambda x:x[0])
        length = len(rides)
        if not length:
            return 0
        dp = [rides[0][2] + rides[0][1] - rides[0][0]] + [0] * (length - 1)
        for i in range(1, length):
            index = -1
            for j in range(i):
                if rides[j][1] <= rides[i][0]:
                    index = j
            if index == -1:
                temp = rides[i][2] + rides[i][1] - rides[i][0]
            else:
                temp = rides[i][2] + rides[i][1] - rides[i][0] + dp[index]
            dp[i] = max(dp[i-1], temp)
        return dp[length-1]


if __name__ == '__main__':
    n = 10
    rides = [[2,3,6],[8,9,8],[5,9,7],[8,9,1],[2,9,2],[9,10,6],[7,10,10],[6,7,9],[4,9,7],[2,3,1]]
    s = Solution()
    res = s.maxTaxiEarnings(n, rides)
    print(res)