def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l + r >> 1
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                l = l + 1
            else:
                r = mid
        return l
