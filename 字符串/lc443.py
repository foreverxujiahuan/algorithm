from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = ""
        cur = ''
        cnt = 0
        for c in chars:
            if c != cur:
                if cur:
                    ans += c
                    if cnt > 1:
                        ans += str(cnt)
                    cnt = 1
                    cur = c
                else:
                    cur = c
                    cnt = 1
            else:
                cnt += 1
        if cur and cnt:
            ans += cur
            if cnt > 1:
                ans += str(cnt)
        return len(ans)


if __name__ == '__main__':
    solution = Solution()
    chars = ["a"]
    res = solution.compress(chars)
    print(res)