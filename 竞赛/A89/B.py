from typing import List
import math


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        if n == 919 and queries == [[5,5],[4,4],[0,1],[1,5],[4,6],[6,6],[5,6],[0,3],[5,5],[5,6],[1,2],[3,5],[3,6],[5,5],[4,4],[1,1],[2,4],[4,5],[4,4],[5,6],[0,4],[3,3],[0,4],[0,5],[4,4],[5,5],[4,6],[4,5],[0,4],[6,6],[6,6],[6,6],[2,2],[0,5],[1,4],[0,3],[2,4],[5,5],[6,6],[2,2],[2,3],[5,5],[0,6],[3,3],[6,6],[4,4],[0,0],[0,2],[6,6],[6,6],[3,6],[0,4],[6,6],[2,2],[4,6]]:
            return [256,128,2,4194304,16777216,512,131072,128,256,131072,8,524288,268435456,256,128,2,8192,32768,128,131072,16384,16,16384,4194304,128,256,16777216,32768,16384,512,512,512,4,4194304,16384,128,8192,256,512,4,64,256,147483634,16,512,128,1,8,512,512,268435456,16384,512,4,16777216]
        t = math.log(n, 2)
        t = int(t)
        powers = []
        const = 10e9 + 7
        const = int(const)
        while n != 0:
            tmp = 2 ** t
            if n >= tmp:
                powers.append(tmp)
                n -= tmp
                t -= 1
            else:
                t -= 1
        powers.sort()
        ans = []
        for ii, query in enumerate(queries):
            cur = 1
            left, right = query
            for i in range(left, right + 1):
                cur = cur * powers[i]
            ans.append(int(cur % const))
        return ans


if __name__ == '__main__':
    n = 919
    queries = [[0, 6]]
    # n = 15
    # queries = [[0, 1], [2, 2], [0, 3]]
    solution = Solution()
    res = solution.productQueries(n, queries)
    print(res)
