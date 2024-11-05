import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv("notebooks/vehicles_us.csv")

st.header("Students Performance")
st.subheader("Exploratory Data Analysis")
st.write("___")
