class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = sorted(s1)
        length = len(a)
        length2 = len(s2)
        for i in range(length2 - length):
            if sorted(s2[i: i+length]) == a:
                return True
        return False
