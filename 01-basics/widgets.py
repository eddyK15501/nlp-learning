import streamlit as st
import pandas as pd

## Title
st.title('Streamlit Text Input')

## Name
name = st.text_input('Enter your name:')

if name:
    st.write(f'Hello, {name}.')
    
## Age
age = st.slider('Select your age', 0, 100, 50)

st.write(f'Your age is {age}.')

## Favorite programming language
options = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favorite programming language:', options)

st.write(f'Your favorite language is {choice}.')

## Pandas DataFrame
data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 32, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

## Streamlit file uploader
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
