
import torch
import numpy as np

cat_entity2index_len = 10
maxlen = 128


entity_masks = np.zeros((10, maxlen, maxlen))

entity_masks[...] = -np.inf
for cat_entity in [2,4,7]:
    entity_masks[cat_entity, :, :] = 0.

print(entity_masks.shape)
print(entity_masks)