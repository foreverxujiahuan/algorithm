from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        arr = []
        for i in range(n+1):
            for j in range(1, i):
                t1 = str(i)
                t2 = str(j)
                arr.append(t2 + "/" + t1)
        ans = set()
        for s in arr:
            n1, n2 = s.split("/")
            n1 = int(n1)
            n2 = int(n2)
            n = self.f(n1, n2)
            n1 = n1 // n
            n2 = n2 // n
            n1 = str(n1)
            n2 = str(n2)
            ans.add(n1 + "/" + n2)
        return list(ans)

    def f(self, a, b):
        if a % b == 0:
            return b
        else:
            return self.f(b, a % b)


if __name__ == '__main__':
    n = 4
    solution = Solution()
    res = solution.simplifiedFractions(n)
    print(res)