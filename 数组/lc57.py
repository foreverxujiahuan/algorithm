from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        nums = set()
        intervals.append(newInterval)
        for interval in intervals:
            start, end = interval
            for i in range(start, end):
                nums.add(i+0.5)
        nums = sorted(list(nums))
        cur = []
        for i in range(len(nums)-1):
            if not cur:
                cur.append(int(nums[i]-0.5))
                if nums[i+1] - nums[i] != 1:
                    cur.append(int(nums[i]+0.5))
                    ans.append(cur)
                    cur = []
            else:
                if nums[i+1] - nums[i] != 1:
                    cur.append(int(nums[i]+0.5))
                    ans.append(cur)
                    cur = []
                else:
                    continue
        if cur:
            cur.append(int(nums[-1] + 0.5))
            ans.append(cur)
        else:
            if nums[-1] > ans[-1][-1]:
                ans.append([int(nums[-1]-0.5), int(nums[-1]+0.5)])
        index_set = set()
        for start, end in ans:
            index_set.update(set(range(start, end+1)))
        for interval in intervals:
            start, end = interval
            if start == end and start not in index_set:
                ans.append([start, end])
        ans.sort(key=lambda d:d[0])
        return ans


if __name__ == '__main__':
    intervals = [[1,5]]
    newInterval = [0,0]
    solution = Solution()
    res = solution.insert(intervals, newInterval)
    print(res)