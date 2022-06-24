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

st.markdown("[![Foo](https://raw.githubusercontent.com/Hezel2000/GeoDataScience/main/icons/flank%20method.jpg)](https://hezel2000-flank-method-flank-data-reduction-2ncvvv.streamlitapp.com)")

st.markdown("[![Foo](icons/flank method.jpg)](https://hezel2000-geodat-start-your-geo-exploration-journey-here-56xkhu.streamlitapp.com)")

st.header('Welcome to the Home of Geoscience Apps')

st.subheader('Choose where to go next:')

st.image('icons/flank method.jpg')