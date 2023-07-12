import streamlit as st
import pandas as pd

st.title("Doing streamlit")
st.write("hey i am deploying a model today")
st.header("This is a header")
df = pd.DataFrame({
    'Name': ['John', 'Adam', 'Bob', 'Mary'],
    'Marks': [98, 90, 89, 76]
})
st.write(df.describe())
