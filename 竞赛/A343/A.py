from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = 0
        score2 = 0
        for i, s in enumerate(player1):
            if 10 in player1[max(i-2, 0): i]:
                score1 += s * 2
            else:
                score1 += s
        for i, s in enumerate(player2):
            if 10 in player2[max(i-2, 0): i]:
                score2 += s * 2
            else:
                score2 += s
        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        else:
            return 0

if __name__ == '__main__':
    player1 = [5, 6, 1, 10]
    player2 = [5, 1, 10, 5]
    solution = Solution()
    res = solution.isWinner(player1, player2)
    print(res)