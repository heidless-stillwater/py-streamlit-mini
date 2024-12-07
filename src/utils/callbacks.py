import streamlit as st    

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
    
