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
geography = st.selectbox('Geography', ohe_geography.categories_[0])
credit_score = st.number_input('Credit Score')
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
tenure = st.slider('Tenure', 0, 10)
balance = st.number_input('Balance')
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
estimated_salary = st.number_input('Estimated Salary')

# Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# One-hot encoded 'Geography' column
geo_encoded = ohe_geography.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=ohe_geography.get_feature_names_out(['Geography']))

# Combine OHE 'Geography' columns with input_data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Predict churn
prediction = model.predict(input_data_scaled)
prediction_probability = prediction[0][0]

# Print prediction
st.write(f'Churn Probability: {prediction_probability:.2f}')

if prediction_probability > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')