
#
d = {'a': 2, "c": 3, "b": 1}
#
# # ans = [['a', 'b', 'c'], [2, 1, 3]]
#
# # print(d.items())
#
# # ans = [[k for k in sorted(d.keys())], [d[k] for k in sorted(d.keys())]]
# # print(ans)
# sored_items = sorted(d.items(), key=lambda x: x[0])
# print(sored_items)

a = [1, 2, 3, 4, 5]
b = ['a', 'c', 'b']
# # ans = [(1, 'a'), (2, 'c'), (3, 'b')]
#
# ans = list(zip(a, b))
# print(ans)
# for k, v in d.items():
#     print(k, v)

for i, j in zip(a, b):
    print(i, j)
