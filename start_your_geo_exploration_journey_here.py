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


st.sidebar.image('https://raw.githubusercontent.com/Hezel2000/GeoROC/main/images/Goethe-Logo.jpg', width=150)


st.header('Welcome to the Home of Geoscience Apps')

st.subheader('Choose where to go next:')

col1, col2, col3 = st.columns(3)

#image width 200 px at 300 dpi resolution

with col1:
    st.markdown("[![Foo](https://raw.githubusercontent.com/Hezel2000/GeoDataScience/main/icons/flank%20method%20small.jpg)](https://hezel2000-flank-method-flank-data-reduction-2ncvvv.streamlitapp.com)")
    st.markdown("[![Foo](https://raw.githubusercontent.com/Hezel2000/GeoDataScience/main/icons/DS-course.jpg)](https://hezel2000-data-science-ds-course-1jyi58.streamlitapp.com)")
    
with col2:
    st.markdown("[![Foo](https://raw.githubusercontent.com/Hezel2000/GeoDataScience/main/icons/MetBase%20Logo.jpg)](https://metbase.org)")
    
with col3:
    st.markdown("[![Foo](https://raw.githubusercontent.com/Hezel2000/GeoDataScience/main/icons/GeoROC%20Viewer.png)](https://hezel2000-georoc-georoc-viewer-oe6zvy.streamlitapp.com/)")