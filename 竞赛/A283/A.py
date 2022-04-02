from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s1, s2 = s.split(":")
        res = []
        ord_id1, ord_id2 = (ord(s1[0]), ord(s2[0]))
        for ch in [chr(ord_id) for ord_id in range(ord_id1, ord_id2 + 1)]:
            for i in range(int(s1[1]), int(s2[1])+1):
                temp = ch + str(i)
                res.append(temp)
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "A1:F1"
    res = solution.cellsInRange(s)
    print(res)