import tensorflow as tf
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

bert_output = tf.constant(bert_output, dtype=float)
mask_input = tf.constant(mask_input, dtype=float)


def compute_sum(mask_input, bert_output):
    """
    计算实体向量的和
    mask_input_shape: batch_size*sequence_length
    bert_output_shape: batch_size*sequence_length*768
    x_sum_shape: batch_size*768
    """
    x0_expend = tf.tile(tf.expand_dims(mask_input, axis=-1), [1, 1, embedding_dim])
    x_sum = tf.reduce_sum((tf.multiply(x0_expend, bert_output)), axis=1)
    return x_sum


def compute_avg(mask_input, bert_output):
    """
    计算实体向量的平均值
    mask_input_shape: batch_size*sequence_length
    bert_output_shape: batch_size*sequence_length*768
    x_avg_shape: batch_size*768
    """
    x_sum = compute_sum(mask_input, bert_output)
    length = tf.expand_dims(tf.reduce_sum(mask_input, axis=1), 1)
    x_avg = tf.divide(x_sum, length)
    return x_avg


sum_ans = compute_sum(mask_input, bert_output)
print(sum_ans)