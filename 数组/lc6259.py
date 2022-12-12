class Allocator:

    def __init__(self, n: int):
        self.size = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        i = -1
        while i < self.n - size + 1:
            i += 1
            if self.size[i: i + size].count(0) != size:
                continue
            for j in range(i, i + size):
                self.size[j] = mID
            return i
        return -1

    def free(self, mID: int) -> int:
        ans = self.size.count(mID)
        for i, n in enumerate(self.size):
            if n == mID:
                self.size[i] = 0
        return ans
