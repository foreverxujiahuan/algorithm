from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        i = 2
        target = 0
        temp = []
        while target < finalSum:
            target += i
            temp.append(i)
            if target == finalSum:
                return temp
            if target > finalSum:
                t = target - finalSum
                return [j for j in temp if j != t]
            i += 2
        return []


if __name__ == '__main__':
    s = Solution()
    finalSum = 28
    res = s.maximumEvenSplit(finalSum)
    print(res)