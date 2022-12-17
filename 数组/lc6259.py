class Allocator:

    def __init__(self, n: int):
        self.size = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        i = 0
        while i < self.n:
            if self.size[i] == 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == size:
                for j in range(i-cnt+1, i+1):
                    self.size[j] = mID
                return i - size + 1
            i += 1
        return -1

    def free(self, mID: int) -> int:
        ans = self.size.count(mID)
        for i, n in enumerate(self.size):
            if n == mID:
                self.size[i] = 0
        return ans


if __name__ == '__main__':
    ans1 = loc = Allocator(10)
    ans2 = loc.allocate(1, 1)
    ans3 = loc.allocate(1, 2)
    ans4 = loc.allocate(1, 3)
    ans5 = loc.free(2)
    ans6 = loc.allocate(3, 4)
    ans7 = loc.allocate(1, 1)
    ans8 = loc.allocate(1, 1)
    ans9 = loc.free(1)
    ans10 = loc.allocate(10, 2)
    ans11 = loc.free(7)
