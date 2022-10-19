class Solution:
    def countTime(self, time: str) -> int:
        ans = 0
        cur_set = set()
        for a in range(0, 10):
            for b in range(0, 10):
                for c in range(0, 10):
                    for d in range(0, 10):
                        t = list(time)
                        if t[0] == '?':
                            t[0] = str(a)
                        if t[1] == "?":
                            t[1] = str(b)
                        if t[3] == '?':
                            t[3] = str(c)
                        if t[4] == '?':
                            t[4] = str(d)
                        cur = "".join(t)
                        if "00" <= cur[:2] <= "23" and "00" <= cur[3:] <= "59" and cur not in cur_set:
                            ans += 1
                            cur_set.add(cur)
        return ans

if __name__ == '__main__':
    time = "??:??"
    solution = Solution()
    res = solution.countTime(time)
    print(res)