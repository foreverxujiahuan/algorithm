from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        length = len(citations)
        citations.reverse()
        candidate = [0]
        for i in range(length):
            if citations[i] >= i+1:
                ans = min(citations[i], i+1)
                candidate.append(ans)
        return max(candidate)


if __name__ == '__main__':
    solution = Solution()
    citations = [0]
    res = solution.hIndex(citations)
    print(res)