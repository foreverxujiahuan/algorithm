import torch

# 创建一个形状为 (16, 5, 20, 20) 的随机 logit 矩阵作为示例
logits = torch.randn(1, 1, 5, 5)

# 定义要筛选的最大值的数量
# seq_length = 2
n = 5
# n = min(n, seq_length * seq_length)
# n = torch.min(n, seq_length * seq_length)
# print(n)
# 展平最后两个维度，并使用 topk 函数获取前 n 大值及其索引
# 新的 shape 将是 (16, 5, 400)
logits_flat = logits.view(1, 1, -1)
values, indices = torch.topk(logits_flat, n)

# 将展平矩阵中的索引转换回原始二维矩阵中的坐标
rows = indices // logits.size(-1)
cols = indices % logits.size(-1)

# 创建一个形状为 (16, 5, n, 3) 的输出矩阵
result = torch.zeros((16, 5, n, 3))

# 填充结果矩阵的最后一维
result[..., 0] = rows
result[..., 1] = cols
result[..., 2] = values

print(result.shape)  # 应该输出 torch.Size([16, 5, 5, 3])
print(result)  # 输出结果矩阵
batch_size, entity_num, seq_len, _ = logits.shape

print(seq_len)
print(type(seq_len))
