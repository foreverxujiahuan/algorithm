from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        small, big, cur = 0, 0, 0
        for diff in differences:
            nxt = cur + diff
            small, big = min(small, nxt), max(big, nxt)
            cur = nxt

        ans = (upper - lower) - (big - small) + 1
        return ans if ans > 0 else 0


if __name__ == '__main__':
    # differences = [93062,-30048,-26193,-81992,-67943,92951,95652,4231,9256,-20548,92518,84150,-19483,-67057,95530,-83994,-95215,83588,-96536,-80032,11593,98648,8867,83148,44559,-55123,91071,36457,-41547,6019,-2618,36518,-32874,89858,17872,22290,96159,-42712,-65545,-16607,7816,-19015,92540,-70869,-88746,-40428,-96659,81704,-7756,80444,64155,-87483,69124,85434,-70336,-75809,-81281,-12913,-57754,-583,77486,3349,-24825,88636,80415,-37736,-86040,37657,44359,-36701,1374,-41792,-32075,-77376,-18179,-62165,-55410,-15056,-13987,243,-76145,-10958,39653,-9446,-56979,-75601,-90924,-13275,66552,-63604,63824]
# -81559
# -68765
#     lower = -81559
#     upper = -68765
    solution = Solution()
    differences = [3,-4,5,1,-2]
    lower = -4
    upper = 5
    res = solution.numberOfArrays(differences, lower, upper)
    print(res)
