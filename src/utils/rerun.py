import streamlit as st 

st.title("Counter example with immediate re-run")

if "count" not in st.session_state:
  st.session_state.count = 0
  
def increment_and_rerun():
  st.session_state.count += 1
  st.rerun()
  
st.write(f"Current count: {st.session_state.count}")

if st.button("Increments and Update immediately"):
  increment_and_rerun()
  