from collections import defaultdict

from sortedcontainers import SortedSet


class NumberContainers:

    def __init__(self):
        self.index2number = {}
        self.number2index = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index2number and self.index2number[index] in self.number2index.keys():
            self.number2index[self.index2number[index]].remove(index)
        self.index2number[index] = number
        self.number2index.setdefault(number, SortedSet()).add(index)

    def find(self, number: int) -> int:
        if number in self.number2index and self.number2index[number]:
            return self.number2index[number][0]
        return -1


if __name__ == '__main__':
    nc = NumberContainers()
    nc.find(10)
    nc.change(2, 10)
    nc.change(1, 10)
    nc.change(3, 10)
    nc.change(5, 10)
    nc.find(10)
    nc.change(1, 20)
    ans = nc.find(10)
    print(ans)
