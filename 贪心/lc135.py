from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        index = ratings.index(min(ratings))
        temp = [1] * len(ratings)
        for i in range(index + 1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                temp[i] = temp[i-1] + 1
            elif ratings[i] < ratings[i-1]:
                temp[i] = temp[i-1] -1
            else:
                temp[i] = min(temp[i-1] - 1, 1)
        for i in range(index-1, -1, -1):
            if ratings[i] > ratings[i+1]:
                temp[i] = temp[i+1] + 1
            elif ratings[i] < ratings[i+1]:
                temp[i] = temp[i+1] - 1
            else:
                temp[i] = min(temp[i+1] - 1, 1)
        print(temp)
        return sum(temp)


if __name__ == '__main__':
    s = Solution()
    ratings = [1,3,2,2,1]
    res = s.candy(ratings)
    print(res)

