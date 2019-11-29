# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:49:52 2019

@author: Thanga
"""

import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
