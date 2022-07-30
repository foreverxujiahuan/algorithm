from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        length = len(arr)
        arr.sort()
        for i in range(length):
            for j in range(length):
                if arr[j] == arr[i] * 2 and i != j:
                    return True
        return False


if __name__ == '__main__':
    arr = [-10, 12, -20, -8, 15]
    solution = Solution()
    res = solution.checkIfExist(arr)
    print(res)