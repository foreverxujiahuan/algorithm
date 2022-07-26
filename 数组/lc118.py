from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = [1]
        ans = []
        for _ in range(numRows):
            ans.append(t)
            cur = [1]
            for i in range(1, len(t)):
                cur.append(t[i]+t[i-1])
            cur.append(1)
            t = cur
        return ans

if __name__ == '__main__':
    n = 1
    solution = Solution()
    res = solution.generate(numRows=n)
    print(res)