import torch

seq_length = 2
topk = 5

input_tensor = torch.tensor([seq_length, topk])
ans = torch.min(input_tensor)
ans = ans.item()
print(ans)
print(type(ans))
