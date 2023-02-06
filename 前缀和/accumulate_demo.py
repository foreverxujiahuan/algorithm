from itertools import accumulate


# 计算前缀和

arr = [1,2,3,4,5]

acc = accumulate(arr)
acc = list(acc)

print(acc)
