from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        toward = "E"
        cnt = 1
        ans = [matrix[0][0]]
        visited[0][0] = True
        i, j = 0, 0
        while cnt < m * n:
            if toward == 'E':
                if j+1 < n and not visited[i][j+1]:
                    ans.append(matrix[i][j+1])
                    visited[i][j+1] = True
                    cnt += 1
                    j += 1
                else:
                    toward = 'S'
            elif toward == 'S':
                if i+1 < m and not visited[i+1][j]:
                    ans.append(matrix[i+1][j])
                    visited[i+1][j] = True
                    cnt += 1
                    i += 1
                else:
                    toward = 'W'
            elif toward == 'W':
                if j-1 >= 0 and not visited[i][j-1]:
                    ans.append(matrix[i][j-1])
                    visited[i][j-1] = True
                    cnt += 1
                    j -= 1
                else:
                    toward = 'N'
            elif toward == 'N':
                if i-1 >= 0 and not visited[i-1][j]:
                    ans.append(matrix[i-1][j])
                    visited[i-1][j] = True
                    cnt += 1
                    i -= 1
                else:
                    toward = 'E'
        return ans


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = solution.spiralOrder(matrix)
    print(res)
