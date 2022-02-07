def minItem(ids, m):
    # write your code here
    id2cnt = dict()
    for i in ids:
        if i in id2cnt.keys():
            id2cnt[i] += 1
        else:
            id2cnt[i] = 1
    cnt_list = list(id2cnt.values())
    cnt_list = sorted(cnt_list)
    res = len(cnt_list)
    for cnt in cnt_list:
        if cnt > m:
            break
        else:
            m -= cnt
            res = res - 1
    return res

ids = [1,1,1,2,2,3]
m = 2
res = minItem(ids, m)
print(res)
