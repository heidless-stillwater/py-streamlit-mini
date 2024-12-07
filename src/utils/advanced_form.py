import streamlit as st 
from datetime import datetime

# from icecream import ic

st.title("Advanced Form")

min_date = datetime(1960, 1, 1)
max_date = datetime.now()

with st.form(key="user_input_form" , clear_on_submit=True):
  
  name1 = st.text_input("Enter your first name")
  
  birth_date = st.date_input("Enter your birth date", min_value=min_date, max_value=max_date)
  
  st.write(f"birth_date: ", birth_date)
 
  
  if birth_date:
    age = max_date.year - birth_date.year
    
    st.write(f"age: ", age)
    st.write(f"min_date: ", min_date)
    st.write(f"max_date: ", max_date)

    if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
      age -= 1
    

  submit_button = st.form_submit_button()
  
  if submit_button:
    st.write("submit pressed")