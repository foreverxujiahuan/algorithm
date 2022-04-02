from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(t):
            cnt = 0
            for cur_t in time:
                cnt += t // cur_t
            return cnt >= totalTrips
        left = 0
        right = totalTrips
        while left<right:
            mid = (right+left-1) // 2
            if check(mid):
                right = left
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    time = [2]
    totalTrips = 1
    solution = Solution()
    res = solution.minimumTime(time, totalTrips)
    print(res)
