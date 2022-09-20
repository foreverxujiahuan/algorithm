from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        ans = 0
        length1, length2 = len(players), len(trainers)
        while i < length1 and j < length2:
            if players[i] <= trainers[j]:
                i += 1
                j += 1
                ans += 1
            else:
                j += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    players = [1,1,1]
    trainers = [10]
    res = solution.matchPlayersAndTrainers(players, trainers)
    print(res)