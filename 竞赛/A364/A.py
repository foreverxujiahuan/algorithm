
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt1 = s.count("1")
        cnt0 = s.count("0")
        s = (cnt1-1) * "1" + cnt0 * "0" + "1"
        ans = int(s, 2)
        return ans