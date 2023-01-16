from collections import Counter, OrderedDict
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        arr = []
        counter = Counter(barcodes)
        for k, v in counter.most_common():
            arr.extend([k] * v)
        ans = [-1 for _ in arr]
        j = 0
        n = len(arr)
        for i in range(0, n, 2):
            ans[i] = arr[j]
            j += 1
        for i in range(1, n, 2):
            ans[i] = arr[j]
            j += 1
        return ans


if __name__ == '__main__':
    barcodes = [7,7,7,8,5,7,5,5,5,8]
    solution = Solution()
    res = solution.rearrangeBarcodes(barcodes)
    print(res)
