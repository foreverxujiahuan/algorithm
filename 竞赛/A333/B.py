from typing import List
import math


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n:
            p = round(math.log(n, 2))
            n = abs(n - 2 ** p)
            ans += 1
        return ans

    def minOperations2(self, n: int) -> int:
        ans = 0
        s = bin(n)[2:]
        s = list(s)
        l = len(s)
        index1, index2 = -1, -1
        while '1' in s:
            for i in range(l-1, -1, -1):
                if s[i] == '1':
                    index1 = i
                    break
            for j in range(index1-1, -1, -1):
                if s[j] == '0' or j == 0:
                    index2 = j
                    break
            for k in range(index2, index1+1):
                s[k] = '0'
            if index2 != 0:
                s[index2-1] = '1'
            ans += 1
        return ans

if __name__ == '__main__':
    n = 54
    solution = Solution()
    res = solution.minOperations2(n)
    print(res)

