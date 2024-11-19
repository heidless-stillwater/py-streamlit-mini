import os
import pandas as pd
import streamlit as st 
from icecream import ic

ic("starting")

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
  