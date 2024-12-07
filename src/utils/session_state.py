import streamlit as st 
from datetime import datetime

from icecream import ic

st.title("Session State")

if "counter" not in st.session_state:
  st.session_state.counter = 0
  
if st.button("increment counter"):
  st.session_state.counter += 1
  st.write("counter encremented to: ", st.session_state.counter)
  
if st.button("reset"):
  st.session_state.counter = 0

st.write(f"Counter value: ", st.session_state.counter)
  
  