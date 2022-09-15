import tensorflow as tf
from skimage import io
import numpy as np
import keras

def image_preprocess(path):
    img = tf.io.read_file(np.array(path).ravel()[0])
    img = tf.image.decode_jpeg(img, channels = 1, ratio = 2)
    img = tf.image.resize(img, [64,64])
    img = img / 255 # This part normalizes the image, scaling it down; 255 is the max, while 0 is the min
    return img

def image_augmentation(img, model_age, model_gender):

	data_augmentation = tf.keras.Sequential([tf.keras.layers.RandomFlip("horizontal_and_vertical"), tf.keras.layers.RandomRotation(0.2)])
	images = []
	images.append(np.array([img]))
	i = 0
	while i < 9:
		img1 = tf.cast(tf.expand_dims(img, 0), tf.float32)
		img1 = data_augmentation(img1)
		images.append(img1)
		i = i+1
	
	predictions_age = []
	predictions_female = []
	predictions_male = []
	for image in images:
		predictions_age.append(model_age.predict(image)[0])
		predictions_female.append(model_gender.predict(image)[0][0])
		predictions_male.append(model_gender.predict(image)[0][1])
    
	return np.mean(predictions_age), np.mean(predictions_female), np.mean(predictions_male)

if __name__ == "__main__":
	search_song()