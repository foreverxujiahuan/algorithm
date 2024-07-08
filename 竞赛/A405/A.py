
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:

        ts = s * 100
        k = k % len(s)
        ans = ""
        for i, c in enumerate(s):
            ans += ts[i+k]
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "fvevzh"
    k = 10
    res = solution.getEncryptedString(s, k)
    print(res)