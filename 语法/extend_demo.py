
a = [1, 2, 3]
b = [2, 3, 4]
c = (1, 2, 3)
d = {"a":1, "b":2}
a.extend(b)  # 拼接全部
print(a)  # [1,2,3,2,3,4]
a.append(b)  # 追加一个
print(a)  # [1,2,3,2,3,4, [2,3,4]]
a.extend(c)
print(a)
a.extend(d)
print(a)
a.extend(d.items())  # d.items(): [("a", 1), ("b", 2)]
print(a)

# for x in d:
#     print(x)