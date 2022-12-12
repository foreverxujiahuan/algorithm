from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        length = len(skill)
        mid = length // 2
        ans = 0
        target = skill[0] + skill[-1]
        for i in range(mid):
            if skill[i] + skill[-i-1] != target:
                return -1
            else:
                ans += skill[i] * skill[-i-1]
        return ans


if __name__ == '__main__':
    skill = [1,1,2,3]
    solution = Solution()
    res = solution.dividePlayers(skill)
    print(res)