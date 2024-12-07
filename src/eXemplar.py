import os
import time
import streamlit as st         
from datetime import datetime
from icecream import ic

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#########
# LAYOUTS
#

# ic("starting")

# text
st.title("layouts")

# sidebar
st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elements within the sidebar.")
sidebar_input = st.sidebar.text_input("enter something on the sidebar")

# tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
  st.write("You are in tab1")

with tab2:
  st.write("You are in tab2")

with tab3:
  st.write("You are in tab3")

# columns
col1, col2, col3 = st.columns(3)
with col1:
  st.header("col1")
  st.write("content for col1")
  
with col2:
  st.header("col2")
  st.write("content for col2")
  
with col3:
  st.header("col3")
  st.write("content for col3")
  
# containers
with st.container(border=True):
  st.write("This is inside a container")
  st.write("Contaners help manage sections of a page")
  
# empty placeholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder")

if st.button("Update placeholder"):
  placeholder.write("the content of this placeholder has been updated")
  
# expander
with st.expander("Expand for more details"):
  st.write("Additional information here")
  st.write("next line")
  
# popover (tooltip)
st.write("hover over this button for a toolip")
st.button("Button with a tooltip", help='this is toolip or popover on hover')

# sidebar input handling
if sidebar_input:
  st.write(f"you entered in the sidebar: {sidebar_input}")
  

############
# CACHE DATA
#
st.title("cache data")
@st.cache_data(ttl=60)
def fetch_data():
  time.sleep(3)   # simulate delay
  return {"data":"this is cached data"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)


################
# CACHE RESOURCE
#
st.title("cache resources")

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

###########
# FRAGMENTS
#
st.title("fragments app")

@st.fragment()
def toggle_and_text():
  cols = st.columns(2)
  cols[0].toggle("Toggle")
  cols[1].text_area("Enter text")
  
@st.fragment()
def filter_and_file():
  new_cols = st.columns(5)
  new_cols[0].checkbox("Filter")
  new_cols[1].file_uploader("Upload image")
  new_cols[2].selectbox("Choose option: ", ["Option 1", "Option 2", "Option 3"])
  new_cols[3].slider("Select value", 0, 100, 50)
  new_cols[4].text_input("Enter text")
  
toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()

#######
# FORMS

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
      

########
# CHARTS
#
# ic("starting")

st.title("Streamlit Charts Demo")

# sample data
chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columns=['A','B','C']
)

# area chart
st.subheader("area chart")
st.area_chart(chart_data)

# bar chart
st.subheader("bar chart")
st.bar_chart(chart_data)

# line chart
st.subheader("line chart")
st.line_chart(chart_data)

# scatter chart
st.subheader("scatter chart")
st.scatter_chart(chart_data)

# map chart
st.subheader("map chart")
map_data = pd.DataFrame(
  np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], 
  columns=["lat", "lon"]
)
st.map(map_data)

# pyplot chart
st.subheader("pyplot chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)

###############
# SESSION STATE
#
if "counter" not in st.session_state:
  st.session_state.counter = 0
  
if st.button("increment counter"):
  st.session_state.counter += 1
  st.write("counter encremented to: ", st.session_state.counter)
  
if st.button("reset"):
  st.session_state.counter = 0

st.title("session state")
st.write(f"Counter value: ", st.session_state.counter)
  
  
############
# RERUN
#

st.title("Counter example with immediate re-run")

if "count" not in st.session_state:
  st.session_state.count = 0
  
def increment_and_rerun():
  st.session_state.count += 1
  st.rerun()
  
st.write(f"Current count: {st.session_state.count}")

if st.button("Increments and Update immediately"):
  increment_and_rerun()
  

################
#
#

# ic("starting")

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

# widgets
st.subheader("widgets")


##########
# CHECKBOX
#

# ic("starting")

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

###########
# CALLBACKS
#

st.title("callbacks")

if "step" not in st.session_state:
  st.session_state.step = 1
  
if "info" not in st.session_state:
  st.session_state.info = {}

def goto_step2(name):
  st.session_state.info["name"] = name
  st.session_state.step = 2

def goto_step1():
  # st.session_state.info["name"] = name
  st.session_state.step = 1

if st.session_state.step == 1:
  st.header("Part 1: info")
  name = st.text_input("Name:", value=st.session_state.info.get("name", ""))
  st.button("next", on_click=goto_step2, args=(name,))
  
elif st.session_state.step == 2:
  st.header("Part 2: review")
  st.subheader("please review this")
  st.write(f"**Name**: {st.session_state.info.get('name', '')}")
  
  if st.button("submit"):
    st.success("Great!")
    st.balloons()
    
  st.button("back", on_click=goto_step1)
    

# text
st.title("widgets")

if "slider" not in st.session_state:
  st.session_state.slider = 25

min_value = st.slider("Set min value: ", 0, 50, 25)

st.session_state.slider = st.slider("Slider: ", min_value, 100, st.session_state.slider)

