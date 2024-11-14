
# import torch
# import torch.nn.functional as F
#
# predict_tensor = torch.randn((8, 50))
# predict_tensor = F.normalize(predict_tensor, p=2, dim=-1)  # L2归一化
# predict_res = torch.matmul(predict_tensor, predict_tensor.T)
#
# print(predict_res)


# numpy的写法
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 假设 X 是一个 m x n 的矩阵，其中每行是一个向量
X = np.random.randn(8, 50)

# 计算余弦相似度矩阵
similarity_matrix = cosine_similarity(X)

print(similarity_matrix)
