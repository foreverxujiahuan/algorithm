from itertools import permutations

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for t in range(1, 11):
            if t * k % 10 == num % 10:
                if t * k <= num:
                    return t
                else:
                    return -1
        return -1


if __name__ == '__main__':
    solution = Solution()
    num = 5
    k = 1
    res = solution.minimumNumbers(num, k)
    print(res)