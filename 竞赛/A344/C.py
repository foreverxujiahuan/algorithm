from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        colors = [0 for _ in range(n+1)]
        cnt = 0
        for query in queries:
            index, color = query
            raw_cnt = 0
            if index != 0 and colors[index] == colors[index-1] and colors[index] != 0:
                raw_cnt += 1
            if index != n-1 and colors[index] == colors[index+1] and colors[index] != 0:
                raw_cnt += 1
            cur_cnt = 0
            colors[index] = color
            if index != 0 and colors[index] == colors[index - 1] and colors[index] != 0:
                cur_cnt += 1
            if index != n - 1 and colors[index] == colors[index + 1] and colors[index] != 0:
                cur_cnt += 1
            diff = cur_cnt - raw_cnt
            cnt = cnt + diff
            ans.append(cnt)
        return ans


if __name__ == '__main__':
    n = 1
    queries = [[0,100000]]
    solution = Solution()
    res = solution.colorTheArray(n, queries)
    print(res)