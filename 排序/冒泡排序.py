# 冒泡排序
def bubbleSort(alist):
    n = len(alist)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


alist = [3,2,4,1]
res = bubbleSort(alist)
print(res)
