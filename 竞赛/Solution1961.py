from typing import List


class Solution:

    def isPrefixString(self, s: str, words: List[str]) -> bool:

        temp = ""
        for word in words:
            temp += word
            if temp == s:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    s = "iloveleetcode"
    words = ["i", "love", "algorithm", "apples"]
    res = solution.isPrefixString(s, words)
    print(res)
