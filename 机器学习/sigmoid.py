import numpy as np

logits_pred = 8



confidence_list = 1 / (1 + np.exp(-logits_pred))

print(confidence_list)