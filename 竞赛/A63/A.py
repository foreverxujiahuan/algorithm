from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        res = 0
        length = len(seats)
        for i in range(length):
            res += abs(students[i] - seats[i])
        return res

if __name__ == '__main__':
    seats = [2,2,6,6]
    students = [1,3,2,6]
    s = Solution()
    res = s.minMovesToSeat(seats, students)
    print(res)
