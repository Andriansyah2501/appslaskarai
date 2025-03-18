import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Hello Word')
st.info('Dashboard Streamlit Andrian Syah')

cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')
 
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)
 
plt.bar(x=cities, height=populations)
plt.show()
