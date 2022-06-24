import streamlit as st
import pandas as pd

st.write("""
    # Kleiner Test
    mit diesem Kram
    """)

st.header('test')

df = pd.read_excel("ChondriteDB.xlsx")

st.write('Ausgabe')
st.write(df.columns)
st.sidebar.multiselect('Chonndrite Class', df['Meteorite Class'].unique(), df['Meteorite Class'].unique()[2])

#st.sidebar.header('ss')
#st.sidebar.selectbox('Element', ['Si', 'Mg', 'Al'])


