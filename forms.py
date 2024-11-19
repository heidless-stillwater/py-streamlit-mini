import os
from icecream import ic

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 

ic("starting")

st.title("Streamlit Form Demo")

with st.form(key="sample_form"):
  
  # text input
  st.subheader("text inputs")
  name = st.text_input("Enter your name:")
  feedback = st.text_area("Provide your feedback:")
  
  # data/time input
  st.subheader("data/time")
  dob = st.date_input("Select your data of birth")
  time = st.time_input("Choose a preferred time")
  
  # selectors
  st.subheader("selectors")
  choice = st.radio("Choose an option:", ["option 0", "option 1", "option 2"])  

  # toggles & checkboobed
  st.subheader("toggles & checkboobed")
  notifications = st.checkbox("Receive notifications?")
  toggle_value = st.checkbox("Enable dark mode")

  st.form_submit_button()
  
  