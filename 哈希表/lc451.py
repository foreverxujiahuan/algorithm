from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        keys = sorted(d.items(), key=lambda d:d[1], reverse=True)
        ans = ""
        for key in keys:
            ans += key[0] * d[key[0]]
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = "tree"
    res = solution.frequencySort(s)
    print(res)