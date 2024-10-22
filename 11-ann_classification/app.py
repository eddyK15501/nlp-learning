import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle

# Load the trained model
model = tf.keras.models.load_model('./model.h5')

# Load the encoders and scaler
with open('./label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)
    
with open('./ohe_geography.pkl', 'rb') as file:
    ohe_geography = pickle.load(file)
    
with open('./scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
    
    
## Streamlit App
st.title('Customer Churn Prediction')

# User input
geography = st.selectbox('Geography', ohe_geography.categories[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])