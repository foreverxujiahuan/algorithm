
import torch

a = torch.Tensor([5])
a.requires_grad = True
print(a)
a.backward()
print(a)
