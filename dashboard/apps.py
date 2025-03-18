import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def app():  
    st.title('Dashboard')
    st.write('Welcome to the dashboard!')

    # Load data
    df = pd.read_csv('data.csv')

    # Display data
    st.write('Data:')
    st.write(df)

    # Display plot
    st.write('Plot:')
    sns.pairplot(df)
    st.pyplot()
