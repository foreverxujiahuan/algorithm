class Solution:
    def isFascinating(self, n: int) -> bool:
        t1, t2 = n * 2, n * 3
        tmp = str(n) + str(t1) + str(t2)
        if "".join(sorted(tmp)) == "123456789":
            return True
        return False
