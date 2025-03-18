import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Hello Word')
st.info('Dashboard Streamlit Andrian Syah')

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.caption('Copyright (c) 2025')
