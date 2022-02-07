from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        distance = {}
        colors2 = []
        for i in colors[:]:
            distance[i] = colors.index(i)

        for j in distance:
            for k in distance:
                colors2.append(abs(distance[j]-distance[k]))

        return max(colors2)


if __name__ == '__main__':
    getmaxdistance = Solution()
    getmaxdistance.maxDistance()
