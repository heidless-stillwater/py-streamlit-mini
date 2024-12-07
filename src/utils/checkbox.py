import os
import pandas as pd
import streamlit as st 
from icecream import ic

ic("starting")

# text
st.title("checkbox")

if "checkbox" not in st.session_state:
  st.session_state.checkbox = False
  st.session_state.user_input = ''

def toggle_input():
  st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show input field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
  st.write("checkbox SET") 
else:
  st.write("checkout NOT SET")

if st.session_state.checkbox == False:
  user_input = st.text_input("Enter something:", value=st.session_state.user_input)
  st.session_state.user_input = user_input
else:
  user_input = st.session_state.get( "user_input", "")

st.write(f"User Input: {user_input}")
