
# import torch
#


import torch

# 创建一个无穷小的标量
infinitesimal = torch.tensor(float('-inf'))

logits = torch.rand((16,3,4))

# 创建一个三维矩阵，这里以3x3x3为例
matrix_shape = (16, 3, 5)

# 使用torch.full来填充矩阵
infinitesimal_matrix = torch.full(matrix_shape, infinitesimal)

concat_matrix = torch.cat([logits, infinitesimal_matrix], dim=-1)

print(concat_matrix)
print(concat_matrix.shape)
print(concat_matrix.device)
