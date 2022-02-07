class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        numbers = [word for word in words if self.f(word)]
        numbers = [int(n) for n in numbers]
        length = len(numbers)
        for i in range(length - 1):
            if numbers[i] >= numbers[i+1]:
                return False
        return True


    def f(self, s):
        for c in s:
            if not '0' <= c <= '9':
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    s = "4 5 11 26"
    res = so.areNumbersAscending(s)
    print(res)