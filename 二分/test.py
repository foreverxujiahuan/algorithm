import time


def my_min(nums):
    ans = 9999999
    for n in nums:
        if n < ans:
            ans = n
    return ans


nums = list(range(32551133))
start = time.time()
my_min(nums)
end = time.time()
t = end - start
print(t)


start = time.time()
min(nums)
end = time.time()
t = end - start
print(t)
