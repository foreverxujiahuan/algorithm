from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(list(word))
        sorted_items = sorted(counter.items(), key=lambda d: d[1], reverse=True)
        sub1 = sorted_items[:8]
        sub2 = sorted_items[8:16]
        sub3 = sorted_items[16:24]
        sub4 = sorted_items[24:]
        ans = 0
        if sub1:
            ans += 1 * sum([t[1] for t in sub1])
        if sub2:
            ans += 2 * sum([t[1] for t in sub2])
        if sub3:
            ans += 3 * sum([t[1] for t in sub3])
        if sub4:
            ans += 4 * sum([t[1] for t in sub4])
        return ans

if __name__ == '__main__':
    soltuion = Solution()
    word = "abcde"
    res = soltuion.minimumPushes(word)
    print(res)
