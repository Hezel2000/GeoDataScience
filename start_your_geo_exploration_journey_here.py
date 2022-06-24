#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")

st.markdown("[![Foo](icons/flank method.jpg)](https://hezel2000-geodat-start-your-geo-exploration-journey-here-56xkhu.streamlitapp.com)")

st.header('Welcome to the Home of Geoscience Apps')

st.subheader('Choose where to go next:')

st.image('icons/flank method.jpg')