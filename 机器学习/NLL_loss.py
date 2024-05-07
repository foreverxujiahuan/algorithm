from torch import nn
import torch


class CrossEntropyLossFromProb(nn.Module):
    def __init__(self):
        super(CrossEntropyLossFromProb, self).__init__()
        self.nllloss = nn.NLLLoss()

    def forward(self, y_pred, y_true):
        # NLLLoss 的 target 需要向量形式
        return self.nllloss(torch.log(y_pred), torch.argmax(y_true, dim=1))


loss_fun = CrossEntropyLossFromProb()

yi = [[[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [1., 1., 1, 1.]]] * 32

yi_pred = [[[0.3123, 0.3296, 0.4067, 0.4],
         [0.3459, 0.3147, 0.2131, 0.4],
         [0.3418, 0.3557, 0.3802, 0.2]]] * 32


yi, yi_pred = torch.tensor(yi), torch.tensor(yi_pred)

print(yi.shape)
print(yi_pred.shape)

loss = loss_fun(yi_pred, yi)
print(loss)
