class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        d = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        l, r = 0, len(s) - 1
        t = 0
        while min(d.values()) < k and l < r:
            t += 1
            if d[s[l]] < k:
                d[s[l]] += 1
                l +=1
            elif d[s[r]] < k:
                d[s[r]] += 1
                r -= 1
            else:
                l += 1
                t += 1
                if d[s[l]] < k:
                    d[s[l]] += 1
                    l += 1

        return t

if __name__ == '__main__':
    s = "aabaaaacaabc"
    k = 2
    solution = Solution()
    res = solution.takeCharacters(s, k)
    print(res)