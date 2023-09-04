class Solution:
    def minimumOperations(self, num: str) -> int:
        n_none = len(num)
        n_00, n_25, n50, n75, n_0 = 100, 100, 100, 100, 100
        length = len(num)
        if '0' in num:
            n_0 = length - 1
        n_00 = self.f(s=num, c1='0', c2='0')
        n_25 = self.f(s=num, c1='2', c2='5')
        n_50 = self.f(s=num, c1='5', c2='0')
        n_75 = self.f(s=num, c1='7', c2='5')
        return min(n_none, n_0, n_25, n_50, n_75, n_00)

    def f(self, s, c1, c2):
        length = len(s)
        ans = 100
        index1 = -1
        index2 = -1
        flag = False
        for i in range(length-1, -1, -1):
            if s[i] == c2:
                index1 = i
                flag = True
                break
        if flag:
            for i in range(index1-1, -1, -1):
                if s[i] == c1:
                    index2 = i
                    break
        if index2 != -1:
            ans = length - index2 - 2
        return ans

if __name__ == '__main__':
    solution = Solution()
    num = "10"
    res = solution.minimumOperations(num)
    print(res)