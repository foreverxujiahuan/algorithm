from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        index1 = []
        index_1 = []
        for i in range(len(forts)):
            if forts[i] == 1:
                index1.append(i)
            elif forts[i] == -1:
                index_1.append(i)
        ans = 0
        for i in index_1:
            for j in index1:
                mi = min(i, j)
                mx = max(i, j)
                t = forts[mi: mx+1]
                if t.count(0) != len(t) - 2:
                    continue
                ans = max(ans, t.count(0))
        return ans

if __name__ == '__main__':
    forts = [0,0,1,-1]
    solution = Solution()
    res = solution.captureForts(forts)
    print(res)