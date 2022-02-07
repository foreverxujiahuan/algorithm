from typing import (
    List,
)

class Solution:
    """
    @param array: An array.
    @return: An interger.
    """
    def findNumber(self, array: List[int]) -> int:
        # Write your code here.
        num2cnt = dict()
        for num in array:
            if num in num2cnt.keys():
                num2cnt[num] += 1
            else:
                num2cnt[num] = 1
        max_num = -1
        res = -1
        for k, v in num2cnt.items():
            if v > max_num:
                max_num = v
                res = k
            elif v == max_num and k < res:
                res = k
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.findNumber([5,5,5,1,1,2,3,3,3,4])
    print(res)
