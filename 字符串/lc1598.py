from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == './':
                continue
            elif log == '../':
                ans = max(0, ans-1)
            else:
                ans += 1
        return ans


if __name__ == '__main__':
    logs = ["./", "wz4/", "../", "mj2/", "../", "../", "ik0/", "il7/"]
    solution = Solution()
    res = solution.minOperations(logs)
    print(res)