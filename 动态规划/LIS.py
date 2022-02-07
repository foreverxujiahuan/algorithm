

def longestIncreasingSubsequence(nums):
    if not nums:
        return 0
    length = len(nums)
    dp = [1] * length
    for i in range(length):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

def longestIncreasingSubsequenceByBinarySearch(nums):
    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            left = 0
            right = len(d) - 1
            loc = right
            while left <= right:
                mid = (left+right) // 2
                if d[mid] >= n:
                    loc = mid
                    right = mid - 1
                else:
                    left = mid + 1
            d[loc] = n
    return len(d)


if __name__ == '__main__':
    nums = [9,3,6,2,7]
    res = longestIncreasingSubsequenceByBinarySearch(nums)
    print(res)
