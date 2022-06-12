import streamlit as st
import pandas as pd

st.write("""
    # Kleiner Test
    
    mit diesem Kram
    """)

st.header('test')

df = pd.read_csv('https://raw.githubusercontent.com/Hezel2000/GeoDataScience/main/data/moessbauer%20standard%20data.csv')

st.write(df)

st.sidebar.header('ss')
st.sidebar.selectbox('Element', ['Si', 'Mg', 'Al'])

fig, ax = plt.subplots()
ax.scatter([1,2,3,4],[1,2,3,4])

st.pyplot(fig)

st.write('test Bokeh')

from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

