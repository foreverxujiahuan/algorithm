from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        first_ch = ''
        for i in range(9, -1, -1):
            if counter.get(str(i)) and counter.get(str(i)) % 2 == 1:
                first_ch = str(i)
                break
        counter[first_ch] = counter[first_ch] - 1
        if first_ch:
            ans = first_ch
        else:
            ans = ''
        for i in range(10):
            if counter.get(str(i)):
                n = counter[str(i)] // 2
                ans = str(i) * n + ans + str(i) * n
        ans = ans.strip("0")
        if not ans:
            return '0'
        return ans



if __name__ == '__main__':
    # num = "00009"
    # num = "00001105"
    num = "444947137"
    # num = "5736732"
    # num = "00011"
    # num = "00000"
    # num = "846853515384906866969100"
    # num = "999944"
    solution = Solution()
    res = solution.largestPalindromic(num)
    print(res)