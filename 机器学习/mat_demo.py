import torch
import torch.nn.functional as F

tensor1 = torch.tensor([[1.,2.],[3.,4.]])
tensor1 = F.normalize(tensor1, p=2, dim=-1)
tensor2 = tensor1.T
mat_res = torch.matmul(tensor1, tensor2)
print(mat_res)
#
#
#
#
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
#
# # 假设 X 是一个 m x n 的矩阵，其中每行是一个向量
# X = np.random.randn(8, 50)
#
# # 计算余弦相似度矩阵
# similarity_matrix = cosine_similarity(X)
#
# print(similarity_matrix)



import torch
import torch.nn.functional as F

A = torch.tensor([[1.,2.],[3.,4.]])
B = A.T

cosine_sim_matrix = F.cosine_similarity(A.unsqueeze(1), B.unsqueeze(0), dim=2)

print(cosine_sim_matrix)

