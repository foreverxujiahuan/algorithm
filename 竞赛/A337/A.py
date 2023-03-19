from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        bin_value = str(bin(n)[2:])[::-1]
        for i, c in enumerate(bin_value):
            if c == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]

if __name__ == '__main__':
    solution = Solution()
    res = solution.evenOddBit(2)
    print(res)