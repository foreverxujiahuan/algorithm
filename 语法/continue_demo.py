#
# i=0
# i=1
# i=2
# i=3

# for i in range(10):
#     if i == 3:
#         break
#     print(i)
#
# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

d = dict()
# key = [1, 2]
key = [1,2,3]

# unhashable: 可变
# hashable: 不可变
d[key] = 3
for k in d:
    print(k)

# def hash():
#
