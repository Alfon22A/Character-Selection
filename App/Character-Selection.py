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
	model_gender = load_model('../Models/Gender_NN3.hdf5')
						   
	img1 = st.file_uploader("Upload a pic!")
	if img1:
		img1 = img1.getvalue()
		img1 = tf.io.decode_image(img1, channels=1)
		img1 = tf.image.resize(img1, [64,64])
		img1 = img1 / 255
		
		age1 = round(model_age.predict((np.array([img1])))[0][0],2)
		female1 = round(model_gender.predict((np.array([img1])))[0][0],2)
		male1 = round(model_gender.predict((np.array([img1])))[0][1],2)
		
		st.write("Age: {:}".format(int(round(age1,0))))
		
		if (female1 > male1) and (female1 >= 0.75):
			st.write("Gender: Female")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age1))
			expander2.write("Female: {:.2%}".format(female1))
			expander2.write("Male: {:.2%}".format(male1))

		elif (male1 > female1) and (male1 >= 0.75):
			st.write("Gender: Male")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age1))
			expander2.write("Female: {:.2%}".format(female1))
			expander2.write("Male: {:.2%}".format(male1))

		else:
			st.write("Gender: Non-binary")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age1))
			expander2.write("Female: {:.2%}".format(female1))
			expander2.write("Male: {:.2%}".format(male1))
		
	img2 = st.camera_input("Or take a pic!")
	if img2:
		img2 = img2.getvalue()
		img2 = tf.io.decode_image(img2, channels=1)
		img2 = tf.image.resize(img2, [64,64])
		img2 = img2 / 255
		
		age2 = round(model_age.predict((np.array([img2])))[0][0],2)
		female2 = round(model_gender.predict((np.array([img2])))[0][0],2)
		male2 = round(model_gender.predict((np.array([img2])))[0][1],2)
		
		st.write("Age: {:}".format(int(round(age2,0))))
		
		if (female2 > male2) and (female2 >= 0.75):
			st.write("Gender: Female")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age2))
			expander2.write("Female: {:.2%}".format(female2))
			expander2.write("Male: {:.2%}".format(male2))

		elif (male2 > female2) and (male2 >= 0.75):
			st.write("Gender: Male")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age2))
			expander2.write("Female: {:.2%}".format(female2))
			expander2.write("Male: {:.2%}".format(male2))

		else:
			st.write("Gender: Non-binary")
			expander2 = st.expander("Know more")
			expander2.write("Age: {:.4}".format(age2))
			expander2.write("Female: {:.2%}".format(female2))
			expander2.write("Male: {:.2%}".format(male2))
main()