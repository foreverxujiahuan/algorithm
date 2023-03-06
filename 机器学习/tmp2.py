import keras
import torch
from keras import backend as K
import tensorflow as tf

def pt_simple_focal_loss(y_pred, y_true, gamma_scale=0.0):
    y_pred = torch.clamp(y_pred, 1e-7, 1 - 1e-7)
    pt = y_true * y_pred + (1 - y_true) * (1 - y_pred)
    corss_entropy_loss = -torch.log(pt)
    gamma_weight = torch.pow(1.0 - pt, gamma_scale)
    focal_loss = gamma_weight * corss_entropy_loss
    focal_loss = torch.sum(focal_loss)
    return focal_loss


y_pred = [[0.1, 0.2, 0.3, 0.4], [0.3, 0.1, 0.1, 0.5]]
y_true = [[0., 0., 0., 1.], [0., 0., 0., 1]]
pt_y_pred, pt_y_true = torch.Tensor(y_pred), torch.Tensor(y_true)
pt_loss = pt_simple_focal_loss(pt_y_pred, pt_y_true, gamma_scale=0.5)
print(pt_loss)

