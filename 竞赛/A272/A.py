from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''

solution = Solution()
words = ["def","ghi"]
print(solution.firstPalindrome(words))