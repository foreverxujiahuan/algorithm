import torch
import torch.nn.functional as F
from torch import nn
import numpy as np


idxs = torch.arange(0, 8, device="cpu")
idxs_1 = idxs[None, :]
idxs_2 = (idxs + 1 - idxs % 2 * 2)[:, None]
labels = torch.eq(idxs_1, idxs_2).float()

temperature = 0.1


def compute_pred_similarity_matrix(y_pred):
    y_pred = F.normalize(y_pred, p=2, dim=-1)  # 句向量l2归一化
    similarities = torch.matmul(y_pred, y_pred.T)  # 相似度矩阵
    similarities = similarities - torch.eye(y_pred.shape[0], device=y_pred.device) * 1e12  # 排除对角线
    similarities = similarities * (1.0 / torch.tensor(temperature))  # scale
    return similarities




# pred_sum_matrix = compute_pred_similarity_matrix(y_pred)


# loss = nn.CrossEntropyLoss()

# raw_loss = loss(pred_sum_matrix, labels)
# print(raw_loss)


class ConbertLoss(nn.Module):
    def __init__(self, temperature=0.1):
        super(ConbertLoss, self).__init__()
        self.temperature = temperature
        self.loss = nn.CrossEntropyLoss()

    def forward(self, y_pred, pos_sample_mask):
        true_matrix = self.compute_true_similarity_matrix(y_pred)
        logit_matrix = self.compute_pred_similarity_matrix(y_pred)
        raw_loss = self.loss(logit_matrix, true_matrix)
        # 要先把pos_sample_mask从矩阵转为向量
        valid_loss = raw_loss * torch.reshape(pos_sample_mask, [-1])  # mask掉反例那些行的loss
        return torch.mean(valid_loss)

    def compute_true_similarity_matrix(self, y_pred):
        idxs = torch.arange(0, y_pred.shape[0], device=y_pred.device)
        idxs_1 = idxs[None, :]
        idxs_2 = (idxs + 1 - idxs % 2 * 2)[:, None]
        labels = torch.eq(idxs_1, idxs_2).float()
        return labels

    def compute_pred_similarity_matrix(self, y_pred):
        y_pred = F.normalize(y_pred, p=2, dim=-1)  # 句向量l2归一化
        similarities = torch.matmul(y_pred, y_pred.T)  # 相似度矩阵
        similarities = similarities - torch.eye(y_pred.shape[0], device=y_pred.device) * 1e12  # 排除对角线
        similarities = similarities * (1.0 / torch.tensor(self.temperature))  # scale
        return similarities


y_pred = torch.randn((8, 50))

pos_sample_mask = [[1],[1],[1],[1],[0],[0],[0],[0]]
pos_sample_mask = np.array(pos_sample_mask)
pos_sample_mask = torch.tensor(pos_sample_mask)
cl = ConbertLoss()
ans = cl(y_pred, pos_sample_mask)
print(ans)

mask = tensor([1, 1, 1, 1, 0, 0, 0, 0])
valid_loss = tensor([3.4079, 3.4079, 3.4079, 3.4079, 0.0000, 0.0000, 0.0000, 0.0000])