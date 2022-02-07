from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        color2houses = dict()
        for i in range(len(colors)):
            color = colors[i]
            if color in color2houses.keys():
                color2houses[color].append(i)
            else:
                color2houses[color] = [i]
        max_len = 0
        for k1, v1 in color2houses.items():
            for k2, v2 in color2houses.items():
                if k1 == k2:
                    continue
                cur_max = max(max(v1) - min(v2), max(v2) - min(v1))
                if cur_max > max_len:
                    max_len = cur_max
        return max_len


if __name__ == '__main__':
    colors = [0,1]
    solution = Solution()
    res = solution.maxDistance(colors)
    print(res)