import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)

t1 = heapq.heappop(nums)
t2 = heapq.heappop(nums)
t3 = heapq.heappop(nums)
print(t1, t2, t3)
