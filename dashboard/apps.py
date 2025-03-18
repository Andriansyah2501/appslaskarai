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
q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
iqr = q75 - q25
cut_off = iqr * 1.5
minimum, maximum = q25 - cut_off, q75 + cut_off
 
outliers = [x for x in data if x < minimum or x > maximum]
with tab2:
    st.header("DATA HARI PADA CHART")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 

st.caption('Copyright (c) 2025')
