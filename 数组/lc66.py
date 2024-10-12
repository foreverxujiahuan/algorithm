from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        digits.reverse()
        num = 0
        for n in digits:
            num += n * flag
            flag *= 10
        num += 1
        ans = []
        while num:
            ans.append(num % 10)
            num = num // 10
        return list(reversed(ans))
