class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        valid = len(sequence) // len(word)
        valid += 1
        ans = valid
        while valid > 0:
            if word * ans in sequence:
                return ans
            ans -= 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    res = solution.maxRepeating(sequence, word)
    print(res)
