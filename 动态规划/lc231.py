class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        a = self.dp_opt(nums[0:len(nums)-1])
        b = self.dp_opt(nums[1:len(nums)])
        return max(a,b)
    def dp_opt(self,arr):
        opt = []
        for i in range(len(arr)):
            opt.append(0)
        opt[0] = arr[0]
        opt[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            A = opt[i - 2] + arr[i]
            B = opt[i - 1]
            opt[i] = max(A, B)
        return opt[len(arr) - 1]