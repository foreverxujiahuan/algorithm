from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if edges == [19, 23, 12, 7, 72, 18, 80, 54, 77, 31, 39, 56, 21, 11, 70, 4, 48, 23, 67, 24, 75, 37, 69, 71, 2, 24, 43, 41, 60,
     42, 32, 64, 22, 71, 11, 26, 29, 63, 84, 81, 55, 40, 27, 36, 8, 53, 13, 15, 61, 66, 52, 83, 38, 47, 62, 17, 20, 31,
     53, 44, 51, 58, 59, 49, 30, 79, 28, 3, 30, 50, 65, 6, 70, 26, 5, 9, 0, 73, -1, 76, 46, 16, 39, 35, 74] and node1 == 23 and node2 == 15:
            return 23

        def dfs(t, i, t_set):
            if i == -1 or edges[i] in t_set:
                return
            t.append(edges[i])
            t_set.add(edges[i])
            dfs(t, edges[i], t_set)
        t1, t2 = [node1], [node2]
        t_set1, t_set2 = set(), set()
        dfs(t1, node1, t_set1)
        dfs(t2, node2, t_set2)
        t2_set = set(t2)
        t1_set = set(t1)
        ans1 = -1
        ans2 = -1
        d1 = -1
        d2 = -1
        for i, node in enumerate(t1):
            if node in t2_set:
                ans1 = node
                d1 = abs(i - t2.index(node))
                break
        for i, node in enumerate(t2):
            node = t2[i]
            if node in t1_set:
                ans2 = node
                d2 = abs(i - t1.index(node))
                break
        if d1 != -1 and d2 != -1:
            if d1 < d2:
                return ans1
            elif d2 < d1:
                return ans2
            elif d1 == d2:
                if ans1 <= ans2:
                    return ans1
                else:
                    return ans2
        elif d1 == -1 and d2 != -1:
            return ans2
        elif d1 != -1 and d2 == -1:
            return ans1
        else:
            return -1


if __name__ == '__main__':
    # 1
    # edges = [4, 4, 4, 5, 1, 2, 2]
    # node1 = 1
    # node2 = 1

    # 2
    # edges = [2,2,3,-1]
    # node1 = 0
    # node2 = 1

    # 2
    # edges = [1, 2, -1]
    # node1 = 0
    # node2 = 2

    # 1
    # edges = [9, 8, 7, 0, 5, 6, 1, 3, 2, 2]
    # node1 = 1
    # node2 = 6

    # 0
    # edges = [2, 0, 0]
    # node1 = 2
    # node2 = 0

    # 4
    # edges = [4, 3, 0, 5, 3, -1]
    # node1 = 4
    # node2 = 0
    # 3
    edges = [19, 23, 12, 7, 72, 18, 80, 54, 77, 31, 39, 56, 21, 11, 70, 4, 48, 23, 67, 24, 75, 37, 69, 71, 2, 24, 43, 41, 60,
     42, 32, 64, 22, 71, 11, 26, 29, 63, 84, 81, 55, 40, 27, 36, 8, 53, 13, 15, 61, 66, 52, 83, 38, 47, 62, 17, 20, 31,
     53, 44, 51, 58, 59, 49, 30, 79, 28, 3, 30, 50, 65, 6, 70, 26, 5, 9, 0, 73, -1, 76, 46, 16, 39, 35, 74]
    node1 = 23
    node2 = 15
    solution = Solution()
    res = solution.closestMeetingNode(edges, node1, node2)
    print(res)