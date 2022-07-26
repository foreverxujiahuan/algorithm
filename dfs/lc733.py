from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        c_color = image[sr][sc]
        def dfs(i, j):
            if image[i][j] != c_color:
                return
            image[i][j] = color
            for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= x < n and 0 <= y < m and image[x][y] == c_color:
                    dfs(x, y)

        if c_color != color:
            dfs(sr, sc)
        return image



if __name__ == '__main__':
    solution = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    res = solution.floodFill(image, sr, sc, newColor)
    print(res)
