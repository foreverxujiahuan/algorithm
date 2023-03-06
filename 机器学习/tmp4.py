import torch
import numpy as np


embedding_dim = 384
batch_size = 16
sequence_length = 128
bert_output = np.random.rand(batch_size, sequence_length, embedding_dim)
mask_input = []
for _ in range(batch_size):
    i = np.random.randint(1, 10)
    cur = [0] * sequence_length
    cur[i] = 1
    mask_input.append(cur)

bert_output = torch.tensor(bert_output)
mask_input = torch.tensor(mask_input)


def compute_sum(mask_input, bert_output):
    x0_expend = torch.tile(torch.unsqueeze(mask_input, dim=-1), [1, 1, embedding_dim])
    x_sum = torch.sum((torch.multiply(x0_expend, bert_output)), dim=-1)
    return x_sum


def compute_avg(mask_input, bert_output):
    x_sum = compute_sum(mask_input, bert_output)
    length = torch.unsqueeze(torch.sum(mask_input, dim=-1), 1)
    x_avg = torch.divide(x_sum, length)
    return x_avg


sum_ans = compute_sum(mask_input, bert_output)
print(sum_ans)

avg_ans = compute_avg(mask_input, bert_output)
print(avg_ans)
