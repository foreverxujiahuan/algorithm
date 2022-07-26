# 选择排序
def selectionSort(alist):
    n = len(alist)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist


alist = [3, 2, 4, 1]
res = selectionSort(alist)
print(res)
