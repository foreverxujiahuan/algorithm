from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.num2cnt = dict()
        self.cnt2num = defaultdict(set)


    def add(self, number: int) -> None:
        if number in self.num2cnt.keys():
            self.num2cnt[number] += 1
        else:
            self.num2cnt[number] = 1
        self.cnt2num[self.num2cnt[number]].add(number)
        if self.num2cnt[number]-1 != 0:
            self.cnt2num[self.num2cnt[number]-1].remove(number)

    def deleteOne(self, number: int) -> None:
        if number in self.num2cnt.keys() and self.num2cnt.get(number) > 0:
            self.num2cnt[number] -= 1
            self.cnt2num[self.num2cnt[number]].add(number)
            self.cnt2num[self.num2cnt[number]+1].remove(number)


    def hasFrequency(self, frequency: int) -> bool:
        if self.cnt2num[frequency]:
            return True
        return False

if __name__ == '__main__':
    freq = FrequencyTracker()
    freq.add(3)
    freq.add(3)
    ans = freq.hasFrequency(2)
    print(ans)