from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_index = []
        b_index = []
        length_s = len(s)
        length_a = len(a)
        length_b = len(b)
        for i in range(length_s - length_a+1):
            if s[i:i+length_a] == a:
                a_index.append(i)
        for i in range(length_s - length_b+1):
            if s[i:i+length_b] == b:
                b_index.append(i)
        ans = []
        for i in a_index:
            for j in b_index:
                if abs(i-j) <= k:
                    ans.append(i)
                    break
        return ans


if __name__ == '__main__':
    s = "isawsquirrelnearmysquirrelhouseohmy"
    a = "my"
    b = "squirrel"
    k = 15
    solution = Solution()
    res = solution.beautifulIndices(s,a,b,k)
    print(res)