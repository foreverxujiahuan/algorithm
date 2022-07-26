from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
        return sum([(c + 2) // 3 for c in d.values()]) if 1 not in d.values() else -1



if __name__ == '__main__':
    tasks = [66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]
    solution = Solution()
    res = solution.minimumRounds(tasks)
    print(res)
