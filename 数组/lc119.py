from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1]
        new_cur = [1]
        for _ in range(rowIndex):
            new_cur = [1]
            for i in range(len(cur)-1):
                new_cur.append(cur[i] + cur[i+1])
            new_cur.append(1)
            cur = new_cur
        return new_cur


if __name__ == '__main__':
    solution = Solution()
    for i in range(10):
        res = solution.getRow(i)
        print(res)


