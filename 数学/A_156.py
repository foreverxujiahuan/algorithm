class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if not intervals: return []

        intervals = sorted(intervals, key=lambda interval: interval.start)

        last, output = None, []
        for interval in intervals:
            if not last or last.end < interval.start:
                output.append(interval)
                last = interval
            else:
                last.end = max(last.end, interval.end)

        return output


if __name__ == '__main__':
    # intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    intervals = [Interval(2,3),Interval(2,2),Interval(3,3),Interval(1,3),Interval(5,7),Interval(2,2),Interval(4,6)]
    solution = Solution()
    merge_intervals = solution.merge(intervals)
    for interval in merge_intervals:
        print(interval.start, interval.end)
