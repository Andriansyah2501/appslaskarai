import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Hello Word')
st.info('Dashboard Streamlit Andrian Syah')

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
plt.hist(jumlah_kucing, bins=4)
plt.show()


