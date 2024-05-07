from torch.nn.functional import cross_entropy
import torch
# Example of target with class indices
input1 = torch.randn(3, 5, requires_grad=True)
target1 = torch.randint(5, (3,), dtype=torch.int64)
loss1 = cross_entropy(input1, target1)

print(input1, target1)
print(loss1)

