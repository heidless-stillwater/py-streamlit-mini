import os
from icecream import ic

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 

ic("starting")

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

