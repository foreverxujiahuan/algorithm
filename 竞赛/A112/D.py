from collections import Counter
from itertools import permutations
from string import ascii_lowercase
from collections import defaultdict


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        counter = Counter(s)
        perm = self.sub("".join(set(s)), k)
        perm = list(perm)
        sum_counter = defaultdict(int)
        mod = 1e9 + 7
        for p in perm:
            cur_sum = sum([counter[c] for c in p])
            sum_counter[cur_sum] += 1
        if not sum_counter.keys():
            return 0
        return int(max([v for k, v in sum_counter.items()]) % mod)

    def sub(self, arr, k):
        finish = []
        size = len(arr)
        end = 1 << size
        for index in range(end):
            array = []
            for j in range(size):
                if (index >> j) % 2:
                    array.append(arr[j])
            if len(array) == k:
                finish.append(array)
        return finish


if __name__ == '__main__':
    s = "abbcd"
    k = 4
    solution = Solution()
    res = solution.countKSubsequencesWithMaxBeauty(s, k)
    print(res)