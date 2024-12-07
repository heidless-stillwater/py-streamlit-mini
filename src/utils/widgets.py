import os
import pandas as pd
import streamlit as st 
from icecream import ic

ic("starting")

# text
st.title("widgets")

if "slider" not in st.session_state:
  st.session_state.slider = 25

min_value = st.slider("Set min value: ", 0, 50, 25)

st.session_state.slider = st.slider("Slider: ", min_value, 100, st.session_state.slider)

