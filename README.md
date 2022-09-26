# Age/Gender Detector

## Introduction

This is an Age/Gender classifier using image processing with Neural Networks.

It contains one Neural Network for each target, age predicted with a regression model and gender with a classification model.

## Data Collection

[Adience Benchmark Gender And Age Classification](https://www.kaggle.com/datasets/ttungl/adience-benchmark-gender-and-age-classification?resource=download)

Data Source contained Age as a group, for example: 25-30 years old, to train the model for regression it was determined that the mean value of the group was used as age.

In order to be inclusive, it has been determined that if the model is unsure about the gender, a Non-binary category is provided.

## Front End

[Character Selection](https://alfon22a-character-selection-web-character-selection-lj9a0x.streamlitapp.com/)

Build with Streamlit
