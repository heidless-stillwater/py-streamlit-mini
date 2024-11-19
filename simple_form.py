import streamlit as st 
from datetime import datetime

from icecream import ic

st.title("User Info Form")

form_values = {
  "name": None,
  "height": None,
  "gender": None,
  "dob": None
}

min_date = datetime(1960, 1, 1)
max_date = datetime.now()

with st.form(key="user_info_form"):
  form_values["name"] = st.text_input("Enter your name:")
  form_values["height"] = st.number_input("Enter your height (cm):")
  form_values["gender"] = st.selectbox("Enter your gender:", ["Male", "Female"])
  form_values["dob"] = st.date_input("Enter your dob:", min_value=min_date, max_value=max_date)
    
  submit_button = st.form_submit_button(label="submit")
  if submit_button:
    if not all(form_values.values()):
      st.warning("Please fill in all of the fields")
    else:
      st.balloons()
      st.write("### info")
      for (key, value) in form_values.items():
        st.write(f"{key}: {value}")
      