
# set_demo = {1, 2, 3, 4}
#
# for c in set_demo:
#     print(c)


# d = {"a": 1, "b": 2}
# # d = {"a": 1}
# for key, value in reversed(d.items()):
#     tmp = d.pop(key)
#     print(tmp)


# lst = [1,2,3,4]
# # [1,2,3,4, [1,2,3,4]]
# # [1,2,3,4, [1,2,3,4], [1,2,3,4, [1,2,3,4]]]
# for i in lst:
#     lst.append(lst)
#
# print(lst)
# lst = [1, 2, 3, 4]
# a = lst.pop()
# # lst.pop()
# print(lst)
# print(a)

# t = d.get("c")
# t1 = d['c']
# print(t)
# tmp = d.pop("c")
# print(d)
# print(tmp)


d = {"a": 1, "b": 2}

if 'c' in d:
    del d['c']
# a_value = d.pop('a')
print(d)
