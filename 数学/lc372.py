from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        cnt = int("".join([str(c) for c in b]))
        return a ** cnt


if __name__ == '__main__':
    a = 2147483647
    b = [2, 0, 0]
    solution = Solution()
    res = solution.superPow(a, b)
    print(res)