

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        ans1 = self.f('r', red, blue)
        ans2 = self.f('b', red, blue)
        return max(ans1, ans2)

    def f(self, flag, red, blue):
        ans = 0
        row = 1
        while True:
            if flag == 'b' and blue >= row:
                ans += 1
                blue -= row
                flag = 'r'
                row += 1
            elif flag == 'r' and red >= row:
                ans += 1
                red -= row
                flag = 'b'
                row += 1
            else:
                break
        return ans

if __name__ == '__main__':
    solution = Solution()
    red = 4
    blue = 9
    res = solution.maxHeightOfTriangle(red, blue)
    print(res)