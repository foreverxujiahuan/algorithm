from itertools import accumulate
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
        for start, end, seats in bookings:
            diff[start-1] += seats
            diff[end] -= seats
        ans = accumulate(diff)
        ans = list(ans)
        return ans[:-1]


if __name__ == '__main__':
    # bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    # n = 5
    bookings = [[1, 2, 10], [2, 2, 15]]
    n = 2
    solution = Solution()
    res = solution.corpFlightBookings(bookings, n)
    print(res)
