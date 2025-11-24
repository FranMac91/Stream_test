import streamlit as st
import pandas as pd
import numpy as np

st.title("Hotel Recommendations System")

DATA_URL = "booking_reviews.csv"
DATE_COLUMN="reviewed_at"

def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis="columns", inplace=True)
    if DATE_COLUMN in data.columns:
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN], errors='coerce')
    
    return data





