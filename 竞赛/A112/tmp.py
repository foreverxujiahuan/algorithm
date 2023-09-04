def sub(arr, k):
    finish=[]    # the list containing all the subsequences of the specified sequence
    size = len(arr)    # the number of elements in the specified sequence
    end = 1 << size    # end=2**size
    for index in range(end):
        array = []    # remember to clear the list before each loop
        for j in range(size):
            if (index >> j) % 2:    # this result is 1, so do not have to write ==
                array.append(arr[j])
        if len(array) == k:
            finish.append(array)
    return [t for t in finish if len(t) == len(set(t))]



def subSet(nums, k):
    if not nums:
        return []
    res = []
    def helper(index , tmp , m):
        if len(tmp) == k:
            res.append(tmp)
        for i in range(index , m):
            helper(i+1,tmp + [nums[i]],m)
    helper(0,[],len(nums))
    return res

arr = "abcd"
ans = subSet(arr, 4)
print(ans)