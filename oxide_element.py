# -*- coding: utf-8 -*-
"""oxide-element.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FOfHh-hXgLW2TAxUEJvhD48Cy233rKe6

## So sweet!
"""

import streamlit as st
import pandas as pd

st.write("""
# First Test
of all this
""")

st.header('Enter an Oxide')
data_input = '1, 2, 3, 4'

inp = st.text_area('Input', data_input, height=200)
inp = inp.splitlines()
inp = ''.join(inp)

st.write('''
    ***
''')

st.header('Your Input')
inp


plt.plot([1,2,3])
st.write(plt.show())