from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        mi = min(counter.values())
        mx = max(counter.values())
        tmp1 = 0
        tmp2 = 0
        for v in counter.values():
            if v - mi > k:  # 减大的
                tmp1 += (v - k - mi)
            if mx - v > k:  # 加小的
                tmp2 += (mx - k - v)
        return min(tmp1, tmp2)

if __name__ == '__main__':
    word = "aabcaba"
    k = 0
    solution = Solution()
    res = solution.minimumDeletions(word, k)
    print(res)
