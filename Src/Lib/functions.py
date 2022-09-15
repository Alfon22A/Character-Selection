import tensorflow as tf
from skimage import io
import numpy as np

def image_preprocess(path):
    img = tf.io.read_file(np.array(path).ravel()[0])
    img = tf.image.decode_jpeg(img, channels = 1, ratio = 2)
    img = tf.image.resize(img, [64,64])
    img = img / 255 # This part normalizes the image, scaling it down; 255 is the max, while 0 is the min
    return img