import streamlit as st
from services.data_loader import load_sales_data, preprocess_data

st.title("AI Sales Data Chatbot")

DATA_PATH = "data/sales_data.xlsb"

try:
    df = load_sales_data(DATA_PATH)
    df = preprocess_data(df)

    st.success("Data loaded successfully ✅")
    st.write("Sample Data:")
    st.dataframe(df.head())

except Exception as e:
    st.error(f"Error loading data: {e}")
