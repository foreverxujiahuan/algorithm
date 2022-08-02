from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        cnt = 0
        i = 1
        while n >= i:
            n -= i
            cnt += 1
            i += 1
        return cnt


if __name__ == '__main__':
    grades = [8,8]
    # [2,31,41,31,36,46,33,45,47,8,31,6,12,12,15,35] 5

    solution = Solution()
    res = solution.maximumGroups(grades)
    print(res)