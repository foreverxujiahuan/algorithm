class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d = dict()
        for i in range(1, 13):
            d[i] = days[i-1]
        day2int = dict()
        i = 0
        for month in range(1, 13):
            if month < 10:
                month_str = '0' + str(month)
            else:
                month_str = str(month)
            for day in range(1, d[month]+1):
                if day < 10:
                    day_str = '0' + str(day)
                else:
                    day_str = str(day)
                cur_s = month_str + '-' + day_str
                day2int[cur_s] = i
                i += 1
        days1 = set(range(day2int[arriveAlice], day2int[leaveAlice] + 1))
        days2 = set(range(day2int[arriveBob], day2int[leaveBob] + 1 ))
        ans = len(days1.intersection(days2))
        return ans

if __name__ == '__main__':
    arriveAlice = "10-01"
    leaveAlice = "10-31"
    arriveBob = "11-01"
    leaveBob = "12-31"
    solution = Solution()
    ans = solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    print(ans)




