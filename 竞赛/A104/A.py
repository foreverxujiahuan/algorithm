from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = [int(detail[11:13]) for detail in details]
        ans = len([age for age in ages if age > 60])
        return ans
