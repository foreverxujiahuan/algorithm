

import re
# 非
pattern = r"\w+"

regex = re.compile(pattern)

text = "AB123我4"

ans = regex.match(text)

print(ans)



# text_list = ['a', 'b', 'c']
# pattern = "\d"
# text = '2' * 18
#
#
# class A:
#     def __init__(self):
#         pattern = "\d+"
#         self.regex = re.compile(pattern)
#
#     def f1(self, text):
#         return re.match(pattern, text)
#
#     def f2(self, text):
#         return self.regex.match(text)
#
# a = A()
#
#
# regex = re.compile(pattern)
# for s in text_list:
#     ans = regex.match(s)
#     print(list(ans))
#
# for s in text_list:
#     ans = re.match(pattern, text)
#     print(ans)


# t = [1, 2, 3]
#
#
# print(t[1])
#
#
# class A:
#     def __index__(self):
#         pass
#
#     def __get__(self, instance, owner):
#         pass

