class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        length = len(blocks)
        ans = 999999
        if length <= k:
            return blocks.count('W')
        for i in range(length - k + 1):
            s = blocks[i: i + k]
            t = s.count("W")
            if t < ans:
                ans = t
        return ans

if __name__ == '__main__':
    solution = Solution()
    blocks = "WWBBBWBBBBBWWBWWWB"
    k=16
    res = solution.minimumRecolors(blocks, k)
    print(res)