import streamlit as st 
# import time

file_path = "example.txt"

@st.cache_resource
def get_file_handler():
  file = open(file_path, "a+")
  return file

file_handler = get_file_handler()

if st.button('Write to file'):
  file_handler.write("New line of text\n")
  file_handler.flush()  # ensure the contents are written immediately
  st.success("Wrote a new line to the file")
  
if st.button("Read file"):
  file_handler.seek(0) # move top the beginning of the file
  content = file_handler.read()
  st.text(content)

st.button("Close File", on_click=file_handler.close)