from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        p2dis = self.get_distance(edges, len(patience) - 1)
        times = []
        length = len(patience)
        for i in range(1, length):
            dis = p2dis[i]
            time = self.get_time(patience[i], dis)
            times.append(time)
        return max(times)

    def get_time(self, pi, dis):
        if int(2 * dis / pi) == 2 * dis / pi:
            temp = int(2 * dis / pi) - 1
        else:
            temp = int(2 * dis / pi)
        return temp * pi + dis * 2 + 1


    def get_distance(self, edges, number):
        p2p = dict()
        for edge in edges:
            p1, p2 = edge
            if p1 in p2p.keys():
                p2p[p1].append(p2)
            else:
                p2p[p1] = [p2]
        p2dis = dict()
        for v in p2p[0]:
            p2dis[v] = 1
        while number != len(p2dis.keys()):
            for p, values in p2p.items():
                for v in values:
                    if v in p2dis.keys() and p in p2dis.keys():
                        p2dis[v] = min(p2dis[v], p2dis[p] + 1)
                    if v not in p2dis.keys() and p in p2dis.keys():
                        p2dis[v] = p2dis[p] + 1
        return p2dis


if __name__ == '__main__':
    edges = [[0,1],[1,2]]
    patience = [0,2,1]
    s = Solution()
    res = s.networkBecomesIdle(edges, patience)
    print(res)
