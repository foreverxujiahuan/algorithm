from collections import defaultdict


class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.nums = []
        self.d = defaultdict(int)

    def consec(self, num: int) -> bool:
        if len(self.nums) >= self.k:
            target = self.nums[-self.k]
            if target in self.d:
                self.d[target] -= 1
        self.nums.append(num)
        self.d[num] += 1
        if len(self.nums) < self.k or num != self.value:
            return False
        if sum(self.d.values()) == self.k and self.d[num] == self.k:
            return True
        return False



if __name__ == '__main__':
    ds = DataStream(2, 2)
    ans1 = ds.consec(1)
    ans2 = ds.consec(1)
    ans3 = ds.consec(2)
    ans4 = ds.consec(2)
    ans5 = ds.consec(1)
    print(ans1, ans2, ans3, ans4, ans5)