from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        mix_arr = []
        length = len(reward1)
        for i in range(length):
            r1, r2 = reward1[i], reward2[i]
            mix_arr.append([r1 - r2, i])
        mix_arr = sorted(mix_arr, key= lambda d:d[0], reverse=True)
        index1 = [i for _, i in mix_arr[: k]]
        index1 = set(index1)
        index2 = set()
        for i, r in enumerate(reward2):
            if i not in index1:
                index2.add(i)
        ans = sum([r for i, r in enumerate(reward1) if i in index1]) +\
              sum([r for i, r in enumerate(reward2) if i in index2])

        return ans

if __name__ == '__main__':
    reward1 = [1,4,4,6,4]
    reward2 = [6,5,3,6,1]
    k = 1
    solution = Solution()
    res = solution.miceAndCheese(reward1, reward2, k)
    print(res)