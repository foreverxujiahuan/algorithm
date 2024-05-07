

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        sub_str_set = set()
        length = len(s)
        for i in range(length-1):
            sub_str_set.add(s[i:i+2])
        reversed_s = "".join(s[::-1])
        for sub_str in sub_str_set:
            if sub_str in reversed_s:
                return True
        return False

if __name__ == '__main__':
    s = "leetcode"
    solution = Solution()
    res = solution.isSubstringPresent(s)
    print(res)