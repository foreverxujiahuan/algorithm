class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while num.endswith("0"):
            num = num[:-1]
        return num