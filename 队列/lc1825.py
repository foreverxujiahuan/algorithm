
from sortedcontainers import SortedList


class MKAverage:

    def __init__(self, m: int, k: int):
        self.nums = SortedList()
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        if len(self.nums) == self.m and num > self.nums[0]:
            self.nums.pop(0)
        self.nums.add(num)

    def calculateMKAverage(self) -> int:
        if len(self.nums) < self.m:
            return -1
        cur = self.nums[self.k: -self.k]
        return sum(cur) // len(cur)


if __name__ == '__main__':
    mk = MKAverage(m=3, k=1)
    mk.addElement(3)
    mk.addElement(1)
    print(mk.calculateMKAverage())
    mk.addElement(10)
    print(mk.calculateMKAverage())
    mk.addElement(5)
    mk.addElement(5)
    mk.addElement(5)
    print(mk.calculateMKAverage())
