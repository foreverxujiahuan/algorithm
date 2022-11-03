from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        set1 = set()
        set2 = set()
        t11, t12 = event1[0], event1[1]
        start1 = int(t11[:2]) * 60 + int(t11[3:])
        end1 = int(t12[:2]) * 60 + int(t12[3:])
        set1 = set1 | set(range(start1, end1+1))

        t21, t22 = event2[0], event2[1]
        start2 = int(t21[:2]) * 60 + int(t21[3:])
        end2 = int(t22[:2]) * 60 + int(t22[3:])
        set2 = set2 | set(range(start2, end2 + 1))

        if set1.intersection(set2):
            return True
        return False

if __name__ == '__main__':
    # event1 = ["01:15", "02:00"]
    # event2 = ["02:00", "03:00"]
    # event1 = ["01:00", "02:00"]
    # event2 = ["01:20", "03:00"]
    event1 = ["10:00", "11:00"]
    event2 = ["14:00", "15:00"]
    solution = Solution()
    res = solution.haveConflict(event1=event1, event2=event2)
    print(res)