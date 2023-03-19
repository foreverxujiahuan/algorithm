import collections
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        length = len(grid)
        cnt = length * length - 1
        visited = [[False for _ in range(length)] for _ in range(length)]
        num2index = dict()
        for row in range(length):
            for col in range(length):
                num2index[grid[row][col]] = (row, col)
        cur = 1
        valid_index = {(row, col) for row in range(length) for col in range(length)}
        while cnt:
            row, col = num2index[cur]
            if (row, col) in valid_index and not visited[row][col]:
                visited[row][col] = True
                cnt -= 1
                cur += 1
                valid_index = {(row + 2, col - 1), (row + 2, col + 1),
                               (row - 2, col + 1), (row - 2, col - 1),
                               (row + 1, col + 2), (row + 1, col - 2),
                               (row - 1, col + 2), (row - 1, col - 2)}
            else:
                break
        return cnt == 0


if __name__ == '__main__':
    grid = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
    solution = Solution()
    res = solution.checkValidGrid(grid)
    print(res)

