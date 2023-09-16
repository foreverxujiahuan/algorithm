import sys


def inverse_num(array):
    n = len(array)
    if n <= 1:
        return 0, array

    mid = n // 2
    # 将数组拆分为二往下递归
    inverse_l, arr_l = inverse_num(array[:mid])
    inverse_r, arr_r = inverse_num(array[mid:])

    nl, nr = len(arr_l), len(arr_r)

    # 插入最大的int作为标兵，可以简化判断超界的代码
    arr_l.append(sys.maxsize)
    arr_r.append(sys.maxsize)

    i, j = 0, 0
    new_arr = []
    # 存储array对应的逆序数
    inverse = inverse_l + inverse_r

    while i < nl or j < nr:
        if arr_l[i] <= arr_r[j]:
            # 插入A[i]的时候逆序数增加j，因为A[i]之前放在这j个元素之前
            inverse += j
            new_arr.append(arr_l[i])
            i += 1
        else:
            new_arr.append(arr_r[j])
            j += 1
    return inverse, new_arr


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    res = inverse_num(nums)
    print(res)