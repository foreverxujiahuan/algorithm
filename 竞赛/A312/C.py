from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        pre_k = set()
        post_k = set()
        length = len(nums)
        i = k
        while i < length - k:
            flag = 1
            for j in range(i-k, i-1):
                if nums[j] < nums[j+1]:
                    flag = 0
                    break
            if flag:
                pre_k.add(i)
                while i < length-k and nums[i] < nums[i+1]:
                    pre_k.add(i)
                    i += 1
            i += 1
        i = k
        while i < length - k:
            flag = 1
            for j in range(i+1, i+k):
                if nums[j] > nums[j+1]:
                    flag = 0
                    break
            if flag:
                post_k.add(i)
                while i < length-k-1 and nums[i+k] <= nums[i+k+1]:
                    post_k.add(i)
                    i += 1
            i += 1
        return sorted(list(post_k.intersection(pre_k)))


if __name__ == '__main__':
    # nums = [878724,201541,179099,98437,35765,327555,475851,598885,849470,943442]
    # k = 4
    # nums = [2, 1, 1, 1, 3, 4, 1]
    # k = 2
    # nums = [2, 1, 1, 2]
    # k = 2
    # nums = [1,2,3]
    # k = 1
    # nums = [83441,339399,879745,789229,406453,100476,71931,60035,18971,172126,420833,798833,945593,987982,993320,994256,997289,998770]
    # k = 5
    solution = Solution()
    # res = solution.goodIndices(nums, k)
    # print(res)


