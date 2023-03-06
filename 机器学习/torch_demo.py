import torch
from torch import nn

a = [[1,2,3], [1,2,6]]
b = [[3], [5]]

a = torch.tensor(a)
b = torch.tensor(b)

ans = torch.divide(a, b)
print(ans)

x = 215235

t = nn.ReLU()