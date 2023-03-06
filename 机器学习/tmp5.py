import tensorflow as tf
import numpy as np
import torch


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

tf_bert_output = tf.constant(bert_output, dtype=float)
tf_mask_input = tf.constant(mask_input, dtype=float)
pt_bert_output = torch.tensor(bert_output)
pt_mask_input = torch.tensor(mask_input)



tf_x0_expend = tf.tile(tf.expand_dims(tf_mask_input, axis=-1), [1, 1, embedding_dim])
tf_x_sum = tf.reduce_sum((tf.multiply(tf_x0_expend, tf_bert_output)), axis=1)

pt_x0_expend = torch.tile(torch.unsqueeze(pt_mask_input, dim=-1), [1, 1, embedding_dim])
pt_x_sum = torch.sum((pt_x0_expend * pt_bert_output), dim=1)


print(tf_x_sum)
print(pt_x_sum)


