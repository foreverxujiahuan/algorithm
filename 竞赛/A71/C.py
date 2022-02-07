class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        temp = []
        m = targetSeconds // 60
        s = targetSeconds - m * 60
        t1 = (m, s)
        if t1[0] < 100:
            temp.append(t1)
        if s < 40 and m >= 1:
            temp.append((m-1, s+60))
        return min([self.cal_time(t[0], t[1], startAt, moveCost, pushCost) for t in temp])

    def cal_time(self, m, s, startAt, moveCost, pushCost):
        m_cost = 0
        s_cost = 0
        m1, m2 = m//10, m % 10
        s1, s2 = s//10, s % 10
        if m == 0:
            m_cost = 0
        elif m1 == 0 and m2 == startAt:
            m_cost += pushCost
        elif m1 == 0 and m2 != startAt:
            m_cost += pushCost + moveCost
        elif m1 == m2 and m1 == startAt:
            m_cost += pushCost * 2
        elif m1 == m2 and m1 != startAt:
            m_cost += pushCost * 2 + moveCost
        elif m1 != m2 and m1 == startAt:
            m_cost += pushCost * 2 + moveCost
        elif m1 != m2 and m1 != startAt:
            m_cost += pushCost * 2 + moveCost * 2
        if m == 0:
            if s1 == 0 and s2 == startAt:
                s_cost += pushCost
            elif s1 == 0 and s2 != startAt:
                s_cost += pushCost + moveCost
            elif s1 == s2 and s1 == startAt:
                s_cost += pushCost * 2
            elif s1 == s2 and s1 != startAt:
                s_cost += pushCost * 2 + moveCost
            elif s1 != s2 and s1 == startAt:
                s_cost += pushCost * 2 + moveCost
            elif s1 != s2 and s1 != startAt:
                s_cost += pushCost * 2 + moveCost * 2
        else:
            if s1 == s2 and s1 == m2:
                s_cost += pushCost * 2
            elif s1 == s2 and s1 != m2:
                s_cost += pushCost * 2 + moveCost
            elif s1 != s2 and s1 == m2:
                s_cost += pushCost * 2 + moveCost
            elif s1 != s2 and s1 != m2:
                s_cost += pushCost * 2 + moveCost * 2
        return s_cost + m_cost


if __name__ == '__main__':
    startAt = 0
    moveCost = 9
    pushCost = 18
    targetSeconds = 6039
    solution = Solution()
    res = solution.minCostSetTime(startAt, moveCost, pushCost, targetSeconds)
    print(res)
