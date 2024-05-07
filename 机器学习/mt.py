import torch
import numpy as np


# a = [[1,2],
#      [3,4]]
#
# # numpy
# vector = np.random.rand(2, 3, 3)
#
# print(vector)
# # 张量
# tensor = torch.tensor(1)
#
# print(a)
# print(tensor)

X = [1, 2, 3, 4]
W = [[1, 2, 3, 4, 1],
     [5, 6, 7, 8, 1],
     [9, 10, 11, 12, 1],
     [13, 14, 15, 16, 1]]
b = [5, 4, 3, 2, 1]


x = 5
a = 6
b = 4
c = 24
x * a * b
x * 24

h1 = 1 * 1 + 2 * 5 + 3 * 9 + 4 * 13
h2 = 1 * 2 + 2 * 6 + 3 * 10 + 4 * 14
h3 = 1 * 3 + 2 * 7
h4 = 0
h5 = 0
H = [h1,h2,h3,h4,h5]
# H + b =[h1 + b1, h2 + b2]
# X = np.random.rand(4)
# H = np.random.rand(5)
# W = np.random.rand()
# print(f"x:{X}")
# print(f"H:{H}")
