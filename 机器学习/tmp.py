import keras
import torch
from keras import backend as K
import tensorflow as tf


def categorical_accuracy(y_true, y_pred):
    return K.cast(K.equal(K.argmax(y_true, axis=-1),
                          K.argmax(y_pred, axis=-1)),
                  K.floatx())

def tf_simple_focal_loss(y_true, y_pred, gamma_scale=0.0):
    epsilon = 1e-7
    y_true = tf.cast(y_true, tf.float32)
    y_pred = tf.clip_by_value(y_pred, epsilon, 1. - epsilon)
    pt = tf.multiply(y_true, y_pred) + tf.multiply(1 - y_true, 1 - y_pred)
    cross_entropy_loss = -tf.math.log(pt)
    gamma_weight = tf.pow(tf.subtract(1., pt), gamma_scale)
    focal_loss = tf.multiply(gamma_weight, cross_entropy_loss)
    return focal_loss


y_pred = [[0.1, 0.2, 0.3, 0.4], [0.3, 0.1, 0.1, 0.5]]
y_true = [[0., 0., 0., 1.], [0., 0., 0., 1]]

tf_y_pred, tf_y_true = tf.constant(y_pred), tf.constant(y_true)


tf_loss = tf_simple_focal_loss(y_true=tf_y_true, y_pred=tf_y_pred, gamma_scale=0.5)

print(tf.math.reduce_sum(tf_loss))

