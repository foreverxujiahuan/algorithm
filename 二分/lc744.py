from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n
        ans = 0
        while l<r:
            mid = l + r >> 1
            if letters[mid] > target:
                ans = mid
                r = mid
            else:
                l = mid + 1
        return letters[ans]


if __name__ == '__main__':
    letters = ["c","f","j"]
    target = "g"
    solution = Solution()
    res = solution.nextGreatestLetter(letters, target)
    print(res)

