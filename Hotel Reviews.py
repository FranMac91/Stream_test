import streamlit as st
import pandas as pd
import numpy as np

st.title("Hotel Recommendations System")

DATA_URL = "booking_reviews.csv"
DATE_COLUMN="reviewed_at"

def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase=lambda x:str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data





