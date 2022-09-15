import streamlit as st
import numpy as np
from keras.models import load_model
import tensorflow as tf

def main ():
	
	st.set_page_config(
		page_title="Character Selection",
		page_icon=":smiley:")

	st.title("Character Selection")
	st.write("Alfonso Muñoz Alonso, 2022")
	st.header("Want to know how the computer sees you?")
	st.write("Disclaimer: this shows how the computer perceives you, the only one who can indentify yourself is you.")
	model_age = load_model('../Models/Age_NN3.hdf5')
	model_gender = load_model('../Models/Gender_NN1.hdf5')
						   
	img1 = st.file_uploader("Upload a pic!")
	if img1:
		img1 = img1.getvalue()
		img1 = tf.io.decode_image(img1, channels=1)
		img1 = tf.image.resize(img1, [64,64])
		img1 = img1 / 255
		
		age1 = round(model_age.predict((np.array([img1])))[0][0],2)
		gender1 = round(model_gender.predict((np.array([img1])))[0][0],2)
		
		st.write("Age: {:}".format(int(round(age1,0))))
		
		if (gender1 <= 0.25):
			st.write("Gender: Female",gender1)
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age1))
			expander2.write("Female: {:.2%}".format(1-gender1))
			expander2.write("Male: {:.2%}".format(gender1))

		elif (gender1 >= 0.75):
			st.write("Gender: Male")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age1))
			expander2.write("Female: {:.2%}".format(1-gender1))
			expander2.write("Male: {:.2%}".format(gender1))

		else:
			st.write("Gender: Non-binary")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age1))
			expander2.write("Female: {:.2%}".format(1-gender1))
			expander2.write("Male: {:.2%}".format1(gender1))
		
	img2 = st.camera_input("Or take a pic!")
	if img2:
		img2 = img2.getvalue()
		img2 = tf.io.decode_image(img2, channels=1)
		img2 = tf.image.resize(img2, [64,64])
		img2 = img2 / 255
		
		age2 = round(model_age.predict((np.array([img2])))[0][0],2)
		gender2 = round(model_gender.predict((np.array([img2])))[0][0],2)
		
		st.write("Age: {:}".format(int(round(age2,0))))
		
		if (gender2 <= 0.25):
			st.write("Gender: Female")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age2))
			expander2.write("Female: {:.2%}".format(1-gender2))
			expander2.write("Male: {:.2%}".format(gender2))

		elif (gender2 >= 0.75):
			st.write("Gender: Male")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age2))
			expander2.write("Female: {:.2%}".format(1-gender2))
			expander2.write("Male: {:.2%}".format(gender2))

		else:
			st.write("Gender: Non-binary")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age2))
			expander2.write("Female: {:.2%}".format(1-gender2))
			expander2.write("Male: {:.2%}".format(gender2))
main()