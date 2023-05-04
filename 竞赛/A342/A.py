
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        ans = arrivalTime + delayedTime
        if ans >= 24:
            return ans - 24
        return ans