import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Hello Word')
st.info('Dashboard Streamlit Andrian Syah')


import streamlit as st
 
st.title('Analisis Data')
tab1, tab2 = st.tabs(["DATA HOUR", "DATA DAY"])
 
with tab1:
    st.header("DATA HARI DALAM CHART")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("DATA HARI PADA CHART")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 

st.caption('Copyright (c) 2025')
