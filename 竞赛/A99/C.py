from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        arr = self.merge(ranges)
        length = len(arr)
        ans = pow(2, length, mod)
        return ans

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    ranges = [[1,3],[10,20],[2,5],[4,8]]
    solution = Solution()
    res = solution.countWays(ranges)
    print(res)