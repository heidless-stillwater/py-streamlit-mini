import os
import pandas as pd
import streamlit as st 
from icecream import ic

ic("starting")

# text
st.title("text")
st.header("header")
st.subheader("subheader")
st.markdown("This is markdown $\sum(s = t)$")
st.caption("caption")

code_example = """
def greet(name):
  print('hello', name)
  
"""
st.code(code_example, language="python")
st.divider()

# images
st.header("images")

# st.image(os.path.join(os.getcwd(), "static", "background.png"))

# dataframe
st.header("dataframe")

st.subheader("Dataframe")
df = pd.DataFrame({
  'Name': ['goliath', ' ceasar', 'zeus'],
  'Age': [25, 32, 37],
  'Occupation': ['god', 'angel', 'devil']  
})
st.dataframe(df)

# data editor
st.subheader("data editor")
editable_df = st.data_editor(df)

# static table
st.subheader("static table")
st.table(df)

# metrics
st.subheader("metrics")
st.metric(label="Total Rows: ", value=len(df))
st.metric(label="Avg Age: ", value=round(df['Age'].mean(), 1))

# JSON & Dict
st.subheader("JSON & dict")
sample_dict = {
  "name" : "alice",
  "age": 25,
  "skills": ["python", "data science", "machine learning"]
}
st.json(sample_dict)

st.write("Dictionary view: ", sample_dict)